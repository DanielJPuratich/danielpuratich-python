## Intro to Game development with PyGame
- Turtle graphics is great for simple drawing but is far too slow and lacks features for game and/or UI development
- We will use a framework called PyGame for more advanced UI and game development
- Games, desktop and mobile apps usually have a GUI - which stands for Graphical User Interface
- A GUI provides buttons and icons, things you can click or drag or manipulate with the keyboard
- PyGame can run on just about any operating system; it has great features for creating 2D and basic 3D games; and is easy to learn
- Modern blockbuster game titles tend to use other game libraries such as Unity, Unreal or even home grown solutions
- But there have been many great games built with PyGame - and the concepts you learn with PyGame are applicable to any kind of game development
- PyGame can be used with imperative code (just functions) or using OO

## Game Loop
- Code runs inside infinite loop
- The loop is called a fixed number of times per second (frames) and we do all work inside the loop
- When we are done, maybe the user hit the escape key, we simply exit the loop to quit
- But we have to know what actions to take for different 'events' -- like key presses, mouse moves and clicks
- For that reason, we usually also have code inside the loop that checks what events happened every time the loop is called
- If an event happened that we care about, like the user hitting the 'Q' key, we can handle it
- **Demo**: ball.py

## Drawing
- PyGame can also draw simple geometric shapes -- but most drawing uses 'Sprites'
- A Sprite is usually just an object that holds an image file (like a PNG) plus some additional information like a size and position
- PyGame uses the upper left corner of the 'screen' to represent the origin (0, 0)
- There are negative X and Y values -- but they are off the visible screen
- One big difference from Turtle is that, usually, each time our loop is called, we clear the screen and redraw everything
- That usually just means doing our drawing inside the game loop
- **Blitting** is what we call drawing one set of pixels (like an image of the hero) on top of another (like our dungeon background image)
- **Demo**: load_image.py

## Animation 
- So how do we animate something? We just adjust its position everytime we draw it inside the loop
- Because our objects have positions and sizes, we can also check where they are on the screen; whether two objects are touching (overlap), etc...
- This is the basis of just about all graphic games -- geometry
- **Demo**: bouncy_ball.py
- **Demo**: stars.py

## Animation Lab - Part 1
- Create a new class that randomly bounces both the ball and a square (you can use any combination of primitives and sprites)
- **Hint**: Review the provided code for ball.py and bouncy.py as well as the documentation links below

## Animation Lab - Part 2
- Print something out to the console anytime the two objects collide
- **Think About**: What constitutes a collision?
- **Hint**: The PyGame Sprite object can provide collision detection -- or you can just detect it yourself

## Animation Lab - Part 3 - Challenge
- Update / copy your code above and do something interesting when objects collide.
- Suggestions:
- Add more sprites / objects
- Make one or both disappear when they collide
- Make one or more stick together when they collide

## Up next
- Simple UI for apps
- Infinite scrolling
- Cell/character animation

#### PyGame References
- Drawing primitives: https://www.pygame.org/docs/ref/draw.html
- Sprites: https://www.pygame.org/docs/ref/sprite.html
- Documentation Home: https://www.pygame.org/docs/
- Flipbook animation: https://www.youtube.com/watch?v=Un-BdBSOGKY
- Game Engine overview: https://www.youtube.com/watch?v=DKrdLKetBZE