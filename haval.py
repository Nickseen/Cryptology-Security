"""
Реализация хеш-функции HAVAL
HAVAL поддерживает 3, 4 или 5 проходов и выходы 128, 160, 192, 224 или 256 бит
Универсальная реализация с настраиваемыми параметрами

Для лабораторной работы № 6 используется Haval192,3:
- 192 бита выхода (24 байта, 48 hex символов)
- 3 прохода (раунда)
"""

import struct

# Константы HAVAL
HAVAL_VERSION = 1
FPTLEN = 32  # длина отпечатка в битах / 32

def _f1(x6, x5, x4, x3, x2, x1, x0):
    """Функция F1"""
    return (x1 & (x0 ^ x4)) ^ (x2 & x5) ^ (x3 & x6) ^ x0

def _f2(x6, x5, x4, x3, x2, x1, x0):
    """Функция F2"""
    return (x2 & ((x1 & ~x3) ^ (x4 & x5) ^ x6 ^ x0)) ^ (x4 & (x1 ^ x5)) ^ (x3 & x5) ^ x0

def _f3(x6, x5, x4, x3, x2, x1, x0):
    """Функция F3"""
    return (x3 & ((x1 & x2) ^ x6 ^ x0)) ^ (x1 & x4) ^ (x2 & x5) ^ x0

def _f4(x6, x5, x4, x3, x2, x1, x0):
    """Функция F4"""
    return (x4 & ((x5 & ~x2) ^ (x3 & ~x6) ^ x1 ^ x6 ^ x0)) ^ (x3 & ((x1 & x2) ^ x5 ^ x6)) ^ (x2 & x6) ^ x0

def _f5(x6, x5, x4, x3, x2, x1, x0):
    """Функция F5"""
    return (x0 & ((x1 & x2 & x3) ^ ~x5)) ^ (x1 & x4) ^ (x2 & x5) ^ (x3 & x6)

def _rotate_right(value, shift):
    """Циклический сдвиг вправо"""
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF

# Перестановки для каждого прохода
_PASS1_ORDER = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

_PASS2_ORDER = [5, 14, 26, 18, 11, 28, 7, 16, 0, 23, 20, 22, 1, 10, 4, 8,
                30, 3, 21, 9, 17, 24, 29, 6, 19, 12, 15, 13, 2, 25, 31, 27]

_PASS3_ORDER = [19, 9, 4, 20, 28, 17, 8, 22, 29, 14, 25, 12, 24, 30, 16, 26,
                31, 15, 7, 3, 1, 0, 18, 27, 13, 6, 21, 10, 23, 11, 5, 2]

_PASS4_ORDER = [24, 4, 0, 14, 2, 7, 28, 23, 26, 6, 30, 20, 18, 25, 19, 3,
                22, 11, 31, 21, 8, 27, 12, 9, 1, 29, 5, 15, 17, 10, 16, 13]

_PASS5_ORDER = [27, 3, 21, 26, 17, 11, 20, 29, 19, 0, 12, 7, 13, 8, 31, 10,
                5, 9, 14, 30, 18, 6, 28, 24, 2, 23, 16, 22, 4, 1, 25, 15]

class Haval:
    """Класс для вычисления HAVAL хеша"""
    
    def __init__(self, passes=4, fpt_len=224):
        """
        Инициализация HAVAL
        passes: количество проходов (3, 4 или 5)
        fpt_len: длина отпечатка в битах (128, 160, 192, 224 или 256)
        """
        self.passes = passes
        self.fpt_len = fpt_len
        self.count = [0, 0]  # количество обработанных бит
        self.fingerprint = [
            0x243F6A88, 0x85A308D3, 0x13198A2E, 0x03707344,
            0xA4093822, 0x299F31D0, 0x082EFA98, 0xEC4E6C89
        ]
        self.block = bytearray(128)
        self.block_index = 0
        
    def update(self, data):
        """Обновление хеша новыми данными"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        for byte in data:
            self.block[self.block_index] = byte
            self.block_index += 1
            
            if self.block_index == 128:
                self._process_block(self.block)
                self.block_index = 0
                
            # Обновляем счетчик битов
            self.count[0] += 8
            if self.count[0] < 8:
                self.count[1] += 1
                
    def _process_block(self, block):
        """Обработка одного блока данных"""
        # Преобразуем блок в 32 32-битных слова
        w = list(struct.unpack('<32I', bytes(block)))
        
        # Сохраняем текущее состояние
        temp = self.fingerprint[:]
        
        # Проход 1
        for i in range(32):
            idx = _PASS1_ORDER[i]
            temp[7] = (_rotate_right(_f1(temp[6], temp[5], temp[4], temp[3], temp[2], temp[1], temp[0]), 7) + 
                      _rotate_right(temp[7], 11) + w[idx]) & 0xFFFFFFFF
            temp = [temp[7]] + temp[0:7]
            
        # Проход 2
        for i in range(32):
            idx = _PASS2_ORDER[i]
            temp[7] = (_rotate_right(_f2(temp[6], temp[5], temp[4], temp[3], temp[2], temp[1], temp[0]), 7) + 
                      _rotate_right(temp[7], 11) + w[idx] + 0x5A827999) & 0xFFFFFFFF
            temp = [temp[7]] + temp[0:7]
            
        # Проход 3
        for i in range(32):
            idx = _PASS3_ORDER[i]
            temp[7] = (_rotate_right(_f3(temp[6], temp[5], temp[4], temp[3], temp[2], temp[1], temp[0]), 7) + 
                      _rotate_right(temp[7], 11) + w[idx] + 0x6ED9EBA1) & 0xFFFFFFFF
            temp = [temp[7]] + temp[0:7]
            
        # Проход 4
        if self.passes >= 4:
            for i in range(32):
                idx = _PASS4_ORDER[i]
                temp[7] = (_rotate_right(_f4(temp[6], temp[5], temp[4], temp[3], temp[2], temp[1], temp[0]), 7) + 
                          _rotate_right(temp[7], 11) + w[idx] + 0x8F1BBCDC) & 0xFFFFFFFF
                temp = [temp[7]] + temp[0:7]
                
        # Проход 5 (если нужен)
        if self.passes >= 5:
            for i in range(32):
                idx = _PASS5_ORDER[i]
                temp[7] = (_rotate_right(_f5(temp[6], temp[5], temp[4], temp[3], temp[2], temp[1], temp[0]), 7) + 
                          _rotate_right(temp[7], 11) + w[idx] + 0xA953FD4E) & 0xFFFFFFFF
                temp = [temp[7]] + temp[0:7]
                
        # Добавляем к текущему состоянию
        for i in range(8):
            self.fingerprint[i] = (self.fingerprint[i] + temp[i]) & 0xFFFFFFFF
            
    def digest(self):
        """Завершение хеширования и возврат результата"""
        # Создаем копию для финализации
        temp_state = Haval(self.passes, self.fpt_len)
        temp_state.fingerprint = self.fingerprint[:]
        temp_state.count = self.count[:]
        temp_state.block = self.block[:]
        temp_state.block_index = self.block_index
        
        # Добавляем padding
        tail_len = temp_state.block_index
        tail = temp_state.block[:tail_len]
        
        # Добавляем бит 1
        tail.append(0x01)
        
        # Определяем, сколько нулей нужно добавить
        if tail_len < 118:
            padding_len = 118 - tail_len - 1
        else:
            padding_len = 246 - tail_len - 1
            
        tail.extend([0] * padding_len)
        
        # Добавляем версию и параметры
        tail.append(((self.fpt_len & 0x03) << 6) | ((self.passes & 0x07) << 3) | (HAVAL_VERSION & 0x07))
        tail.append((self.fpt_len >> 2) & 0xFF)
        
        # Добавляем длину сообщения (64 бита)
        bit_length = (self.count[1] << 32) | self.count[0]
        tail.extend(struct.pack('<Q', bit_length))
        
        # Обрабатываем финальные блоки
        for i in range(0, len(tail), 128):
            block = tail[i:i+128]
            if len(block) == 128:
                temp_state._process_block(block)
                
        # Обрезаем результат до нужной длины
        num_words = self.fpt_len // 32
        result = b''.join(struct.pack('<I', temp_state.fingerprint[i]) for i in range(num_words))
        
        return result
        
    def hexdigest(self):
        """Возвращает хеш в шестнадцатеричном виде"""
        return self.digest().hex()

def haval224_4(data):
    """Вспомогательная функция для вычисления Haval224,4"""
    h = Haval(passes=4, fpt_len=224)
    h.update(data)
    return h.hexdigest()
