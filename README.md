# Wandbinhood #

![Example Image](./assets/example.png)

For the intersection of gambling, deep learning, and unix ricing (wip)

## Example Usage ##

To run the example plot:

```
git clone https://github.com/spikedoanz/wandbinhood/
cd wandbinhood
pip install -r requirements.txt
flask run
```

To make your own plots with live updates, then also do:

```
from wandbinhood import create_project, append project

project_name = 'example'
create_project(project_name, ['loss', 'accuracy'])

epochs = 100
for epoch in epochs:
    ### Training code ###
    # loss = something
    # accuracy = something else
    apppend_project(project_name, [loss, accuracy])
```

The flask server at 5000 will then plot your results in real time

## Notes ##

This is not meant to be a complete project, this is just something I hacked together for a different project

How it works:

1. do a training run
2. push whatever numbers you want to a csv
3. flask run in the background
    3.1 watch the csv
    3.2 every column gets its own plot

## Some cool features I could add but am lazy ##

- [ ] Candlestick plots
- [ ] Guides for working with cloud training
- [ ] Different color schemes (catppuccin), and an easy switcher in config file

