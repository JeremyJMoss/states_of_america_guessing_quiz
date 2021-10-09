import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Enter a states name.").title()

    for state in data.state:
        if state == answer_state:
            correct_state = data[data.state == answer_state]
            x_cor = int(correct_state.x)
            y_cor = int(correct_state.y)
            pen.goto(x_cor, y_cor)
            pen.write(answer_state, align="center", font=("Arial", 10, "normal"))
            correct_guesses.append(answer_state)


screen.exitonclick()
