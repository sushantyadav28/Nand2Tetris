
import sys
import os
import re

# Nand2Tetris Capstone Assembler
# Student K = 65
# Extra feature: Duplicate label warning

K = 65

# Predefined symbols
SYMBOLS = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576
}

for i in range(16):
    SYMBOLS["R" + str(i)] = i

# Hack computation codes
COMP = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "M": "1110000",
    "!D": "0001101", "!A": "0110001", "!M": "1110001",
    "-D": "0001111", "-A": "0110011", "-M": "1110011",
    "D+1": "0011111", "A+1": "0110111", "M+1": "1110111",
    "D-1": "0001110", "A-1": "0110010", "M-1": "1110010",
    "D+A": "0000010", "D+M": "1000010",
    "D-A": "0010011", "D-M": "1010011",
    "A-D": "0000111", "M-D": "1000111",
    "D&A": "0000000", "D&M": "1000000",
    "D|A": "0010101", "D|M": "1010101"
}

DEST = {
    "": "000", "M": "001", "D": "010",
    "MD": "011", "A": "100", "AM": "101",
    "AD": "110", "AMD": "111"
}

JUMP = {
    "": "000", "JGT": "001", "JEQ": "010",
    "JGE": "011", "JLT": "100", "JNE": "101",
    "JLE": "110", "JMP": "111"
}


def clean_file(filename):
    instructions = []

    with open(filename, "r") as file:
        for line_number, line in enumerate(file, 1):
            line = line.split("//")[0].strip()
            line = line.replace(" ", "").replace("\t", "")

            if line:
                instructions.append((line, line_number))

    return instructions


def first_pass(instructions):
    rom_address = 0
    variables = SYMBOLS.copy()
    labels = set()

    for instruction, line_number in instructions:

        if instruction.startswith("(") and instruction.endswith(")"):
            label = instruction[1:-1]

            if not re.fullmatch(r"[A-Za-z_.$:][A-Za-z0-9_.$:]*", label):
                raise ValueError(
                    f"Line {line_number}: Invalid label"
                )

            if label in labels:
                print(
                    f"WARNING: Duplicate label '{label}' "
                    f"at line {line_number}"
                )
            elif label in SYMBOLS:
                print(
                    f"WARNING: Label '{label}' conflicts "
                    f"with a predefined symbol at line {line_number}"
                )
            else:
                variables[label] = rom_address
                labels.add(label)

        else:
            rom_address += 1

    return variables


def second_pass(instructions, symbols):
    machine_code = []
    next_variable = 16

    for instruction, line_number in instructions:

        if instruction.startswith("("):
            continue

        # A-instruction
        if instruction.startswith("@"):
            value = instruction[1:]

            if value.isdigit():
                address = int(value)

            else:
                if not re.fullmatch(
                    r"[A-Za-z_.$:][A-Za-z0-9_.$:]*", value
                ):
                    raise ValueError(
                        f"Line {line_number}: Invalid symbol"
                    )

                if value not in symbols:
                    symbols[value] = next_variable
                    next_variable += 1

                address = symbols[value]

            if not 0 <= address <= 32767:
                raise ValueError(
                    f"Line {line_number}: Address out of range"
                )

            binary = format(address, "016b")
            machine_code.append(binary)

        # C-instruction
        else:
            dest = ""
            jump = ""

            if "=" in instruction:
                dest, instruction = instruction.split("=")

            if ";" in instruction:
                comp, jump = instruction.split(";")
            else:
                comp = instruction

            if comp not in COMP:
                raise ValueError(
                    f"Line {line_number}: Invalid computation"
                )

            if dest not in DEST:
                raise ValueError(
                    f"Line {line_number}: Invalid destination"
                )

            if jump not in JUMP:
                raise ValueError(
                    f"Line {line_number}: Invalid jump"
                )

            binary = "111" + COMP[comp] + DEST[dest] + JUMP[jump]
            machine_code.append(binary)

    return machine_code, symbols


def assemble(input_file):
    print("Nand2Tetris Capstone Assembler")
    print("K =", K)

    instructions = clean_file(input_file)

    symbols = first_pass(instructions)

    machine_code, symbols = second_pass(
        instructions, symbols
    )

    output_file = os.path.splitext(input_file)[0] + ".hack"

    with open(output_file, "w") as file:
        for code in machine_code:
            file.write(code + "\n")

    print("Assembly completed successfully!")
    print("Instructions:", len(machine_code))
    print("Output file:", output_file)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python assembler.py file.asm")

    else:
        try:
            assemble(sys.argv[1])

        except (ValueError, OSError) as error:
            print("ERROR:", error)
