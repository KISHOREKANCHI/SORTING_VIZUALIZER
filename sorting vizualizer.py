#ARRAY
import random
arr=[]
for i in range(15):
    arr.append(random.randint(1,50))



#SORTING
def SelectionSort(arr):
    l=len(arr)
    for i in range(l):
        min=arr[i]
        changes=0
        for j in range(i+1,l):
            if arr[j]<min:
                changes=1
                min=arr[j]
                m=j
        if changes==1:
            arr[i],arr[m]=arr[m],arr[i]
        graph(arr)
def BubbleSort(arr):
    l=len(arr)
    switches=1
    while switches!=0:
        switches=0
        for i in range(l-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                switches=1
            graph(arr)
def InsertionSort(arr):
    l=len(arr)
    sort=[]
    sort.append(arr[0])
    for i in range(1,l):
        sort.append(arr[i])
        x=len(sort)-1
        while sort[x]<sort[x-1] and x>0:
            sort[x],sort[x-1]=sort[x-1],sort[x]
            x-=1
            graph(sort)
def MergeSort(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        MergeSort(left)
        MergeSort(right)
        i,j,k=0,0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
            graph(arr)
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
            graph(arr)
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
            graph(arr)
def QuickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop(0)
        left=[]
        right=[]
        xyz=[]
        graph(xyz)
        for i in arr:
            if i>pivot:
                right.append(i)
            else:
                left.append(i)
        xyz=QuickSort(left)+[pivot]+QuickSort(right)
def HeapSort(arr):
    def MaxHeap(arr,n,ParentIndex):
        largest=ParentIndex
        left=2*ParentIndex+1
        right=2*ParentIndex+2
        if left<n and arr[left]>arr[largest]:
            largest=left
        if right<n and arr[right]>arr[largest]:
            largest=right
        if largest!=ParentIndex:
            arr[largest],arr[ParentIndex]=arr[ParentIndex],arr[largest]
            MaxHeap(arr,n,largest)
    def heapsort(arr):
        n=len(arr)
        for i in range(n//2-1,-1,-1):
            MaxHeap(arr,n,i)
            graph(arr)
        for i in range(n-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i]
            MaxHeap(arr,i,0)
            graph(arr)




#BUTTONS
from tkinter import *
from tkinter.ttk import*
root=Tk()
root.geometry("350x350")
def selection():
    root.destroy()
    t.write("SELECTION SORT")
    impliment()
    SelectionSort(arr)

def bubble():
    root.destroy()
    t.write("BUBBLE SORT")
    impliment()
    BubbleSort(arr)
  
def insertion():
    root.destroy()
    t.write("INSERTION SORT")
    impliment()
    InsertionSort(arr)

def merge():
    root.destroy()
    t.write("MERGE SORT")
    impliment()
    MergeSort(arr)
   
def quick():
    root.destroy()
    t.write("QUICK SORT")
    impliment()
    QuickSort(arr)

def heap():
    root.destroy()
    t.write("HEAP SORT")
    impliment()
    HeapSort(arr)


    
#GRAPHS
import turtle
from turtle import getscreen
t= turtle.Turtle()
t.speed(1000)
turtle.screensize(20000,20000)
t.hideturtle()
def impliment():
    wn =turtle.Screen()
    wn.bgcolor("light blue")
    wn.title("Turtle")
    t.up()
    t.backward(700)
    t.left(90)
    t.forward(300)
    t.dot()
    t.down()
    t.left(180)
    t.forward(600)
    t.left(90)
    t.forward(700)
    t.up()
    t.backward(700)
    t.down()
    SelectionSort(arr)
    turtle.done()
    SelectionSort(arr)
def graph(arr):
    l=len(arr)
    for i in range(l):
        t.forward(15)
        t.left(90)
        t.forward(arr[i]*1.25)
        t.write(arr[i])
        t.dot()
        t.backward(arr[i]*1.25)
        t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(300)
    t.backward(300)
    t.right(90)
    



SELECTION=Button(root,text="SELECTION SORT",command=selection)
SELECTION.place(x=50,y=50)
BUBBLE=Button(root,text="BUBBLE SORT      ",command=bubble)
BUBBLE.place(x=50,y=100)
INSERTION=Button(root,text="INSERTION SORT",command=insertion)
INSERTION.place(x=50,y=150)
MERGE=Button(root,text="MERGE SORT      ",command=merge)
MERGE.place(x=50,y=200)
QUICK=Button(root,text="QUICK SORT       ",command=quick)
QUICK.place(x=50,y=250)
HEAP=Button(root,text="HEAP SORT         ",command=heap)
HEAP.place(x=50,y=300)
root.mainloop()



            

