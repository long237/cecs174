import musicbox
NOTES =[('C', 60), ('D', 62), ('E', 64), ('F', 65), ('G', 67), ('A', 69), ('B', 71)]
MAJOR_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MINOR_INTERVALS = [2, 1, 2, 2, 1, 2, 2]
my_music = musicbox.MusicBox()
#def main():
#    m = musicbox.MusicBox()
#    m.play_note(60, 1000)
#    m.play_chord([60, 64, 67], 1000)
#    m.close()

def note_to_int(note):
    num_octave = note.rfind('^') + 1
    remaining_note = note[num_octave:]
    user_letter = remaining_note[0]
    symbol = note[len(note)-1]
    user_int = 0
    symbol_int = 0
    # check user letter to tuple letter
    for note_tuple in NOTES:
        (note_letter, note_int) = note_tuple
        if note_letter == user_letter:
            user_int = note_int
    # if statement for the note letter
    if user_int == 0:
        return -1
    # if statements for the symbols
    # user_letter will equal symbol if there are no 'b' or '#' after the note.
    # if there is 'b' or '#' after the note, run the code below.
    if user_letter != symbol:
        if symbol == 'b':
            symbol_int = -1
        elif symbol == '#':
            symbol_int = 1
        else:
            return -1
    return user_int + (12 * num_octave) + symbol_int

def print_menu():
    print('1.Play scale')
    print('2.Play song')
    print('3.Quit')

def get_menu_choice():
    user_input = -1
    while user_input < 1 or user_input > 3:
        user_input = int(input("Select a function: "))
    return user_input

def get_scale():
    note_int = ''
    user_scale = ''
    # while loop condition:
    # note_int is to validate the note the user enter such as ('C'). Keep running as long as
    # the user enter the wrong letter
    # user_scale is to validate 'major' or minor.
    # Keep running as long as the user enter the wrong note letter or the wrong scale.
    while note_int == -1 or (user_scale != 'major' and user_scale != 'minor'):
        user_input = input('Enter a scale:')
        split_input = user_input.split(' ')
        user_scale = split_input[1]
        note_int = note_to_int(split_input[0])
    if user_scale == 'major':
        return (note_int, 'major')
    if user_scale == 'minor':
        return (note_int, 'minor')

def scale_to_int(scale):
    (note_int, user_scale) = scale
    notes = [note_int]
    #if scale is a major add note_int with the major interval
    if user_scale == 'major':
        for i in range(len(MAJOR_INTERVALS)):
            note_int += MAJOR_INTERVALS[i]
            notes.append(note_int)
    #if scale is a minor, add note_int with the minor interval
    else:
        for i in range(len(MINOR_INTERVALS)):
            note_int = note_int + MINOR_INTERVALS[i]
            notes.append(note_int)
    return notes

def menu_play_scale():
    user_input = get_scale()
    notes_to_play = scale_to_int(user_input)
    for note in notes_to_play:
        my_music.play_note(note,500)


def get_song_file():
    user_input = input('Enter name of file to play song from: ')
    return user_input

def play_song(file_name):
    song = []
    note = ''
    for line in open(file_name):
        line_split = line.split(" ")
        # skip line that has '"//"'
        if line_split[0] == '//':
            continue
        duration = int(line_split[(len(line_split)-1)].strip())
        # checking if there is only one note to play
        if line_split[0] == 'P':
            note = 'P'
        elif line_split[0] == 'I':
            note = 'I'
        elif len(line_split) == 2:
            note = note_to_int(line_split[0])
        # if there are more than one note in the line_split, add the note into the list.
        elif len(line_split) > 2:
            list_of_int = []
            note_list = line_split[0:len(line_split)-1]
            for note_letter in note_list:
                note_int = note_to_int(note_letter)
                list_of_int.append(note_int)
            list_and_duration = (list_of_int, duration)
            # add the tuple into the list and start move to the next iteration
            song.append(list_and_duration)
            continue
        #create a list of tuples with packages contain notes info
        note_and_duration = (note,duration)
        song.append(note_and_duration)
    for note_to_play in song:
        (note, duration) = note_to_play
        if note == "P":
            my_music.pause(duration)
        # fixme after changing the instrument, program does not reverse back to the original one.
        elif note == 'I':
            my_music.change_instrument(duration)  # this duration is suppose to be an instrument number
        elif isinstance(note,list) == True:
            my_music.play_chord(note,duration)
        else:
            my_music.play_note(note, duration)

def menu_play_song():
    user_input = get_song_file()
    play_song(user_input)


def main():
    user_input = -1
    while user_input != 3:
        while user_input < 1 or user_input > 3:
            print_menu()
            user_input = int(input('Pick a function: '))
        if user_input == 1:
            menu_play_scale()
        elif user_input == 2:
            menu_play_song()
        elif user_input == 3:
            print("Goodbye")
            break
        user_input = -1



main()
my_music.close()
