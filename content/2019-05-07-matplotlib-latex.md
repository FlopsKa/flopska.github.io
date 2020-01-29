Title: Nice LaTeX Plots with Matplotlib
Date: 2019-05-07
Category: computer science
Summary: For my thesis I want the plots from jupyter notebook to integrate well with the rest of the LaTeX document. The article shows the settings necessary to achieve this look consistently by modifying the `matplotlibrc`. Using this approach the correct settings are always used and I can't forget them.

There exist various ways to use LaTeX fonts in the matplotlib plots. When I first googled this I came upon embedding `*.pgf` files directly into the document which is then supposed to use the same font as the rest of the document. However I had problems with the correct size of the resulting images.

Now I embed the `*.pdf` files directly which has the added advantage that it is easy to preview the files without running LaTeX. Before I always saved two files per image: One pdf for viewing, one pgf for including.

## Setup

### matplotlibrc

The following settings are necessary in the `matplotlibrc` file. Create this file if it does not exist and put it in the folder from which you run your notebooks. I think it's pretty self-explanatory what each setting does, otherwise the [matplotlib-help](https://matplotlib.org/users/usetex.html) is of great value.

```ini

axes.labelsize     : 12
axes.titlesize     : 14
figure.titlesize   : 14
legend.fontsize    : 10
savefig.bbox       : tight
xtick.labelsize    : 10
ytick.labelsize    : 10

font.cursive       : Zapf Chancery
font.family        : lmodern
font.monospace     : Courier, Computer Modern Typewriter
font.sans-serif    : Helvetica, Avant Garde, Computer Modern Sans serif
font.serif         : Times, Palatino, New Century Schoolbook, Bookman, Computer Modern Roman
font.size          : 10

pgf.rcfonts 	   : False

text.usetex        : true

```

### Jupyter Notebook

To save to a pdf file from your notebook:

```python
plt.savefig('figures/correlation.pdf')
```

### LaTeX document

In the LaTeX document the image can be included using this code:

```latex
\begin{figure}[h!]
   \centering
   \includegraphics[scale=0.8]{figures/correlation.pdf}
   \caption{The value of the incremental correlation coefficient computed for two random variables.}
   \label{fig:correlation-coefficient}
\end{figure}
``` 

Also you have to add

```latex
\usepackage{lmodern}
```

to your front matter.

### Result

The resulting image looks like this, I think it's pretty neat.

![Incremental Correlation Coefficient]({static}/images/correlation.png)

The sizes can also be adopted separately for each plot. For more information on font sizes, look [here](
https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot).

Edit: [KarelZe](http://github.com/KarelZe) showed me another way to achieve this result: https://gist.github.com/KarelZe/778b77dcc8dd30e59dae8f14c139eb28
