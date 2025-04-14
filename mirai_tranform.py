#!/usr/bin/env python3
from binaryninja import Transform
from binaryninja.enums import TransformType

class XOR_MIRAI(Transform):
    name = 'XOR_MIRAI'
    long_name = 'XOR_MIRAI'
    transform_type = TransformType.InvertingTransform
    group = "XOR"

    @staticmethod
    def xorkey(data, key):
        output = []
        for byte in data:
            output.append(byte ^ key)
        return bytes(output)

    def perform_encode(self, data, params):
        return self.xorkey(data, 0x22)

XOR_MIRAI.register()
