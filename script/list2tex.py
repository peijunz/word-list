#!/usr/bin/env python3
from pronlib import *
fp=open('../toefl-wym/wymrev','r')
head=r'''\documentclass[12pt]{article}
\usepackage[top=1in,bottom=1.1in,left=1.2in,right=0.9in]{geometry}
\usepackage{ctex}
\usepackage{tipa}
\newcommand{\eng}[1]{\fbox{#1}\index{#1}\quad}
\newcommand{\chn}[1]{\emph{#1}}
\newcommand{\pron}[1]{[\textipa{#1}]\quad}
\begin{document}
\title{托福词汇表}
\author{王玉梅}
\date{}
\maketitle
\noindent
\setlength{\parindent}{-0.3in}

'''
tail=r'''\end{document}'''
print(head)
for i in fp:
    eng,chn=i[:-1].split('\t')
    eng=eng.strip()
    p=yb(eng,prpt(chn))
    if p:
        pron2tex(p)
        print('\\eng{'+eng+'}\\pron{'+pron2tex(ame(p))+'}\\chn{'+chn+'}\n')
    else:
        print('\\eng{'+eng+'}'+'\\chn{'+chn+'}\n')
print(tail)
