from coding_exercise.domain.model.cable import Cable


class Splitter:

    def __validate(self):
        valid = True
        if not valid:
            raise ValueError

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate()

        splits = []     # This is the list varible to store the splitted cable, in other words it is returned cable list. 

        num_splits = times+1        # If we split the initial cable split "n" times, then the cable is splitted in "n+1" pieces. It represents the total number of pieces.
        split_len = cable.length // (num_splits)    # The length of each equal piece is the longest integer length cable.
        remainder_len = cable.length % (num_splits) # The length remainder is the cable, and its length is less than num_splits

        #if the length of each splitted piece is zero, in case original cable length is small than splitting times "n"
        if split_len == 0:
            splits.append(cable) #no splitting
        else:
            # if the length of remainder is longger than splitted part, then we can split again the remainder.
            #loop
            while remainder_len > split_len:
                remainder_len -= split_len # split the cable with the same equal length as equally splitted.
                num_splits +=1      # the number of pieces is increased

            #Adding the cable pieces to the result list, with name "coconuts-xx" and splitted length. 
            for ind in range(num_splits):
                if num_splits>10:
                    name = f"coconuts-{ind:02}" # if the total count of pieces is bigger than 10, the name is formatted "coconuts-" followed by 2digits number.
                else:
                    name = f"coconuts-{ind}" # else, the name is formatted "coconuts-" followed by 1 digit number.
                split = Cable(split_len, name) #create Cable class instance using split_len, and name
                splits.append(split)    #append at the last of the result list to be returned
        return splits   # return result

