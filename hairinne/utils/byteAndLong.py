from enum import Enum


class Endian(Enum):
    LITTLE_ENDIAN = 0
    BIG_ENDIAN = 1


def toBytearray(
        a: int,
        range_: int = 8,
        endian: Endian = Endian.LITTLE_ENDIAN
) -> bytearray:
    res = bytearray()
    for i in range(range_):
        print(a)
        res.append((a >> (i * 8)) & 0xFF)
    return res if endian is Endian.LITTLE_ENDIAN else res[::-1]


def toLong(
        a: bytearray,
        range_: int = 8,
        endian: Endian = Endian.LITTLE_ENDIAN
) -> int:
    res = 0
    use = bytearray(a) if endian is Endian.LITTLE_ENDIAN else bytearray(a)[::-1]
    for i in range(range_):
        res |= use[i] << (i * 8)
    return res


def getFromEnd(a: bytearray, length: int) -> bytearray:
    """
      Returns a bytearray from the end of a bytearray
      and source array will lose the bytes.

      @param a: The bytearray to get from

      @param length: The length of the bytearray to get

      @return: The bytearray that was gotten
    """
    res = bytearray()
    for i in range(length):
        res.append(a[-i - 1])
        a.pop()
    return res[::-1]
