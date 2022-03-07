from time import sleep


class Carousel:
    def __init__(self, display, pictures):
        # to show numbers of pictures
        self.display = display
        self.pictures = pictures

    def display_pictures(self, i):
        length = len(self.pictures)
        return f"-| {self.pictures[i % length]} |-"
    
    def show(self, turn, start_index):
        # to limit turns for testing purpose
        turn = turn
        # to choose the starting picture's index
        start_index = start_index

        # infinite loop(carousel suppose nonstop looping)
        # continue_loop = True
        # while continue_loop:
        #   # action

        while turn > 0:
            sleep(1)
            print_str = ""
            multiple_display = start_index

            for _ in range(self.display):
                print_str += self.display_pictures(multiple_display)
                multiple_display += 1

            print(print_str)
            turn -= 1
            start_index += 1


pictures = ["Picture A", "Picture B", "Picture C", "Picture D", "Picture E", "Picture F"]

carousel = Carousel(display=2, pictures=pictures)
carousel.show(turn=10, start_index=2)