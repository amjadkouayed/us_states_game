import turtle
import pandas

screen = turtle.Screen()
screen.title("welcome to the us states game")
image = "blank_states_img.gif"
screen.setup(725, 491)

screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")

guess_count = 0
game_on = True
while guess_count < 50:
    answer_state = screen.textinput(f"Guess the state {guess_count}/50", "whats a state's name").title()


    all_states = list(states.state)

    if answer_state in all_states:
        guess_count += 1
        picked_state = states[states.state == answer_state]
        states_x = int(picked_state["x"])
        states_y = int(picked_state["y"])

        t = turtle.Turtle()
        t.hideturtle()
    else: 
        continue


    def print_text(x, y, text):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.write(text, font=("Arial", 10, "normal"))


    print_text(states_x, states_y, answer_state)




turtle.mainloop()


