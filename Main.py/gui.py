from tkinter import* 
w_width = 1440
w_height = 700
bg_color= "#00000"

window=Tk()
window.geometry(str(w_width) +"x"+ str(w_height))
window.title("My app")

top_frame= Frame(background='green', width=w_width, height=100)
top_frame.pack()

main_frame= Frame(background='red', width=w_width, height= (w_height - 200))
main_frame.pack

bottom_frame = Frame(background='blue', width=w_width, height=100) 
bottom_frame.pack

home_button = Button(bottom_frame, text="Home", height = 5, width = 5, bg= 'black')
home_button.place(x=0,y=0)
window.mainloop() 