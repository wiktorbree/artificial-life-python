# artificial-life-python

Simple python script that simulate artificial life, **based on a video on YouTube by Brainxyz**. He made this in `javascript`. 
It's pretty simple and only takes 81 lines of code in Python but surely it can be achieved with less lines.
You can experiment with it as much as you want.
 

## Adding/Changing colors/particles
If you want to add new particles just put `[name] = create([amount], [color])` right outside of the `while running` loop. 


If you want to change colours you can edit lines that look like this `[name] = create([amount], [color])`. For example I want to change red particles `red = create(300, (255, 0, 0))` to only create 50 of them and make them blue. I'll write `red =  create(50, (0, 0, 255))`


<img width="324" alt="Screenshot 2023-12-17 at 21 10 56" src="https://github.com/wiktorbree/artificial-life-python/assets/44704582/513541dd-922e-4103-af62-8ec35f115959">

## Making rules
To add more rules to the simulation write `rule([particle1], [particle2], [force (g)])` inside the `while running` loop under `win.fill((0, 0, 0))`.


<img width="255" alt="Screenshot 2023-12-17 at 21 12 32" src="https://github.com/wiktorbree/artificial-life-python/assets/44704582/d8ea441b-8e45-450a-b981-f5f506119daa">

## Important!
Have fun with it and remember this script was made based on a [YouTube video by Brainxyz](https://www.youtube.com/watch?v=0Kx4Y9TVMGg) where he made this in `javascript`. So please go and show him some love :)
