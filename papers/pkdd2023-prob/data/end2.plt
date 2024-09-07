#set terminal pdfcairo size 500,450 enhanced font 'Verdana,9'
#set size 1,1
set encoding utf8
set xlabel font ",15"
set ylabel font ",15"
set title font ",35"
set key font ",15"
set yrange [-6:50]
set ylabel "full test acc - hypothesis-only acc (%)"
set xlabel "Datasets"
set output "end.png"
unset tics
set xtics font ",13"
set ytics font ",13"

set ytics -5,5,50

set origin 0,0
set lmargin 10
set rmargin 3
set tmargin 2
set bmargin 6
set boxwidth 1
set xlabel offset 0,-1
set ylabel offset -0.5,0
set xtics ('SNLI' 0, 'QNLI' 1, 'MNLI' 2, 'ROCStory' 3, 'COPA' 4, 'SWAG' 5, 'RACE' 6, 'RECLOR' 7, 'ARCT' 8, 'ARCT\_adv' 9,)

#set xtics center offset 0,-1
set style histogram clustered gap 2   #//gap 2表示裂隙宽等于矩形宽度的2倍
#set style fill pattern border -1 #//fill solid表示完全填充柱体，后面跟0-1的参数，1表示完全填充，border 表示柱体的边线颜色，-1表示黑色。这里还可以加参数pattern
set style fill pattern 1
plot 'end2.txt' using 11 with histogram title 'FT', \
    "" using 12 with histogram title 'ES', \
    "" using 13 with histogram title 'BT', \
    "" using 14 with histogram title 'RT'#//using 1 表示d2.data数据中的第一列，using 1:3表示第一列和第三列
