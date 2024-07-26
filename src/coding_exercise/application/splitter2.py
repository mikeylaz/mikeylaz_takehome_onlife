from coding_exercise.domain.model.cable import Cable

class Splitter:
    def __validate(self, cable, times):
        if not (1 <= times <= 64):
            raise ValueError("The number of splits 'times' must be between 1 and 64.")
        if not (2 <= cable.length <= 1024):
            raise ValueError("Cable length must be between 2 and 1024.")
        if cable.length <= times:
            raise ValueError("The cable cannot be split into more pieces than its length.")

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate(cable, times)

        num_pieces = times + 1
        piece_length = cable.length // num_pieces
        remainder_length = cable.length % num_pieces

        pieces = []

        # Create primary pieces with adjusted lengths considering the remainder
        for i in range(num_pieces):
            # Adjusting each piece length by adding one from the remainder until exhausted
            adjusted_length = piece_length + (1 if i < remainder_length else 0)
            pieces.append(Cable(adjusted_length, f"coconuts-{i:02}"))

        return pieces
