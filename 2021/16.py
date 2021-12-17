#!/usr/bin/python3

from aoctools import InputReader

def calc_value_of_operator(packet_type_id, results):
    if packet_type_id == 0: return sum(results)
    elif packet_type_id == 1:
        value = 1
        for res in results:
            value *= res
        return value
    elif packet_type_id == 2: return min(results)
    elif packet_type_id == 3: return max(results)
    elif packet_type_id == 5: return 1 if results[0] > results[1] else 0
    elif packet_type_id == 6: return 1 if results[0] < results[1] else 0
    elif packet_type_id == 7: return 1 if results[0] == results[1] else 0
    return 'ERROR'

def parse_packet(packet_binary):
    packet_version = int(packet_binary[0:3], 2)
    packet_binary = packet_binary[3:]

    version_sum = packet_version

    packet_type_id = int(packet_binary[0:3], 2)
    packet_binary = packet_binary[3:]

    # Packets with type ID 4 represent a literal value.
    if packet_type_id == 4:
        literal_val_bin, stop = '', False
        while not stop:
            literal_val_bin += packet_binary[1:5]
            if packet_binary[0] == '0': stop = True
            packet_binary = packet_binary[5:]

        return version_sum, packet_binary, int(literal_val_bin, 2)

    # ELSE: any packet with a type ID other than 4 represents an operator
    type_id = int(packet_binary[0])
    packet_binary = packet_binary[1:]

    results = []

    # If the length type ID is 0, then the next 15 bits are a number that represents the total 
    # length in bits of the sub-packets contained by this packet.
    if type_id == 0:
        length_of_subpackets = int(packet_binary[0:15], 2)
        packet_binary = packet_binary[15:]

        subpacket_binary = packet_binary[0:length_of_subpackets]
        while len(subpacket_binary) > 0:
            v_sum, subpacket_binary, res = parse_packet(subpacket_binary)
            results.append(res)
            version_sum += v_sum

        return version_sum, packet_binary[length_of_subpackets:], calc_value_of_operator(packet_type_id, results)

    # ELSE: If the length type ID is 1, then the next 11 bits are a number that represents the number 
    # of sub-packets immediately contained by this packet.
    number_of_subpackets = int(packet_binary[0:11], 2)
    packet_binary = packet_binary[11:]

    for _ in range(0, number_of_subpackets):
        v_sum, packet_binary, res = parse_packet(packet_binary)
        results.append(res)
        version_sum += v_sum

    return version_sum, packet_binary, calc_value_of_operator(packet_type_id, results)

# get the input
packet_hex = InputReader.strings('./input/16.txt')[0]

# convert the input to a binary string
packet_bin = ''
for p in packet_hex: packet_bin += bin(int(p, 16))[2:].zfill(4)

# calculate and print the results
print('Part 1: ' + str(parse_packet(packet_bin)[0])) # 957
print('Part 2: ' + str(parse_packet(packet_bin)[2])) # 744953223228