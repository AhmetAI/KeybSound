import time
import pynput
from pynput.keyboard import Key, Listener
import pygame
import threading
from tkinter import *
from tkinter import font
from tkinter import filedialog
import os
from tkinter import messagebox
import shutil
import random
import signal

def show_frame(frame):
    frame.tkraise()

window = Tk()
window.geometry("500x500+370+100")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.title("KeybSound")
window.resizable(False, False)
icon = PhotoImage(file = "images//icon.png")
window.iconphoto(True, icon)


anaekran = Frame(window, bg="#5454c5")
harfayarekran = Frame(window, bg="#5454c5")
muzikayarekran = Frame(window, bg="#5454c5")

for frame in (anaekran, harfayarekran, muzikayarekran):
    frame.grid(row=0, column=0, sticky='nsew')


dizin = ''
muzik_dosya_yolu = ''
filename = ''
dosya = ''
uzanti = ''



#------Def------

def tumunusec():
    harf_a.set(1)
    harf_b.set(1)
    harf_c.set(1)
    harf_d.set(1)
    harf_e.set(1)
    harf_f.set(1)
    harf_g.set(1)
    harf_h.set(1)
    harf_i.set(1)
    harf_j.set(1)
    harf_k.set(1)
    harf_l.set(1)
    harf_m.set(1)
    harf_n.set(1)
    harf_o.set(1)
    harf_p.set(1)
    harf_r.set(1)
    harf_s.set(1)
    harf_t.set(1)
    harf_u.set(1)
    harf_v.set(1)
    harf_y.set(1)
    harf_z.set(1)
    harf_w.set(1)
    harf_x.set(1)
    harf_q.set(1)

def tmunukaldir():
    pygame.mixer.quit()
    harf_a.set(0)
    harf_b.set(0)
    harf_c.set(0)
    harf_d.set(0)
    harf_e.set(0)
    harf_f.set(0)
    harf_g.set(0)
    harf_h.set(0)
    harf_i.set(0)
    harf_j.set(0)
    harf_k.set(0)
    harf_l.set(0)
    harf_m.set(0)
    harf_n.set(0)
    harf_o.set(0)
    harf_p.set(0)
    harf_r.set(0)
    harf_s.set(0)
    harf_t.set(0)
    harf_u.set(0)
    harf_v.set(0)
    harf_y.set(0)
    harf_z.set(0)
    harf_w.set(0)
    harf_x.set(0)
    harf_q.set(0)

def anaekrandon():
    show_frame(anaekran)

def harfayar():
    show_frame(harfayarekran)

def muzikayar():
    show_frame(muzikayarekran)







#-----Müzik Ayarlar-----


#------AnaEkran------

baslikfont = font.Font(size="24", underline=1)
baslik = Label(anaekran, text="KeybSound", fg="#7f007f", bg="#5454c5", font=baslikfont).place(relx="0.35", rely="0.01")

harfayaryazifont = font.Font(size="17", underline=1)
harfayaryazi = Label(anaekran, text="Harf Ayarları", font=harfayaryazifont, bg="#5454c5", fg="#342056").place(relx="0.37", rely="0.2")

harfayarfont = font.Font(size="13")
harfayarbuton = Button(anaekran, text="Ayarlara Git", bg="#5454c5", fg="#342056",activeforeground="#342056",activebackground="#639cd9", font=harfayarfont, command=harfayar).place(relx="0.41", rely="0.28")

sesayarfont = font.Font(size="17", underline=1)
sesayaryazi = Label(anaekran, text="Ses Ayarları", bg="#5454c5", fg="#342056", font=sesayarfont).place(relx="0.37", rely="0.5")

sesayarbtnfont = font.Font(size="13")
sesayarbuton = Button(anaekran, text="Ayarlara Git", bg="#5454c5", fg="#342056",activeforeground="#342056",activebackground="#639cd9", font=sesayarbtnfont, command=muzikayar).place(relx="0.40", rely="0.58")


#-----Discord----

dcfont = font.Font(size="12")
dcyazi = Label(anaekran, text="Discord:\ntroool_#1447", bg="#5454c5", fg="#342056", font=betafont).place(relx="0.02", rely="0.90")


#------HarfAyarları------

harfbaslikfont = font.Font(size="20", underline=1)
harfbaslik = Label(harfayarekran, text="Harf Ayarları", bg="#5454c5", fg="#342056", font=baslikfont).place(relx="0.35", rely="0.01")

harfacklmfont = font.Font(size="15")
harfacklm = Label(harfayarekran, text="Aktifleştirmek istediğiniz harfi işaretleyin.", bg="#5454c5", fg="#342056", font=harfacklmfont).place(relx=0.17, rely=0.13)

harf_a = IntVar()
harf_a_cb = Checkbutton(harfayarekran, text="A", variable=harf_a, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5", font="Times 22 bold").place(relx=0.05, rely=0.2)

harf_b = IntVar()
harf_b_cb = Checkbutton(harfayarekran, text="B", variable=harf_b, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.05, rely=0.3)

harf_c = IntVar()
harf_c_cb = Checkbutton(harfayarekran, text="C", variable=harf_c, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.05, rely=0.4)

harf_d = IntVar()
harf_d_cb = Checkbutton(harfayarekran, text="D", variable=harf_d, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.05, rely=0.5)

harf_e = IntVar()
harf_e_cb = Checkbutton(harfayarekran, text="E", variable=harf_e, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.05, rely=0.6)

harf_f = IntVar()
harf_f_cb = Checkbutton(harfayarekran, text="F", variable=harf_f, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.05, rely=0.7)

harf_g = IntVar()
harf_g_cb = Checkbutton(harfayarekran, text="G", variable=harf_g, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.05, rely=0.8)

harf_h = IntVar()
harf_h_cb = Checkbutton(harfayarekran, text="H", variable=harf_h, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.28, rely=0.2)

harf_i = IntVar()
harf_i_cb = Checkbutton(harfayarekran, text="i", variable=harf_i, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.28, rely=0.3)

harf_j = IntVar()
harf_j_cb = Checkbutton(harfayarekran, text="J", variable=harf_j, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.28, rely=0.4)

harf_k = IntVar()
harf_k_cb = Checkbutton(harfayarekran, text="K", variable=harf_k, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.28, rely=0.5)

harf_l = IntVar()
harf_l_cb = Checkbutton(harfayarekran, text="L", variable=harf_l, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.28, rely=0.6)

harf_m = IntVar()
harf_m_cb = Checkbutton(harfayarekran, text="M", variable=harf_m, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.28, rely=0.7)

harf_n = IntVar()
harf_n_cb = Checkbutton(harfayarekran, text="N", variable=harf_n, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.28, rely=0.8)

harf_o = IntVar()
harf_o_cb = Checkbutton(harfayarekran, text="O", variable=harf_o, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.51, rely=0.2)

harf_p = IntVar()
harf_p_cb = Checkbutton(harfayarekran, text="P", variable=harf_p, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.51, rely=0.3)

harf_r = IntVar()
harf_r_cb = Checkbutton(harfayarekran, text="R", variable=harf_r, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.51, rely=0.4)

harf_s = IntVar()
harf_s_cb = Checkbutton(harfayarekran, text="S", variable=harf_s, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.51, rely=0.5)

harf_t = IntVar()
harf_t_cb = Checkbutton(harfayarekran, text="T", variable=harf_t, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.51, rely=0.6)

harf_u = IntVar()
harf_u_cb = Checkbutton(harfayarekran, text="U", variable=harf_u, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.51, rely=0.7)

harf_v = IntVar()
harf_v_cb = Checkbutton(harfayarekran, text="V", variable=harf_v, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.51, rely=0.8)

harf_y = IntVar()
harf_y_cb = Checkbutton(harfayarekran, text="Y", variable=harf_y, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.74, rely=0.2)

harf_z = IntVar()
harf_z_cb = Checkbutton(harfayarekran, text="Z", variable=harf_z, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.74, rely=0.3)

harf_w = IntVar()
harf_w_cb = Checkbutton(harfayarekran, text="W", variable=harf_w, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.74, rely=0.4)

harf_x = IntVar()
harf_x_cb = Checkbutton(harfayarekran, text="Z", variable=harf_x, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.74, rely=0.5)

harf_q = IntVar()
harf_q_cb = Checkbutton(harfayarekran, text="Q", variable=harf_q, onvalue=1, offvalue=0, bg="#5454c5",activebackground="#5454c5",selectcolor="#5454c5",font="Times 22 bold").place(relx=0.74, rely=0.6)


tmunusecfont = font.Font(size="10")
tmunusecbtn = Button(harfayarekran, text="Tümünü Seç", bg="#5454c5", fg="#342056",activeforeground="#342056",activebackground="#639cd9",font=tmunusecfont, command=tumunusec).place(relx=0.70, rely=0.73)

tmunukldrfont = font.Font(size="10")
tmunukldrbtn = Button(harfayarekran, text="Tümünü Kaldır", bg="#5454c5", fg="#342056",activeforeground="#342056",activebackground="#639cd9",font=tmunukldrfont, command=tmunukaldir).place(relx=0.70, rely=0.83)

kntrlbtnfont = font.Font(size="15")
kntrlbtn = Button(harfayarekran, text="Kaydet", font=kntrlbtnfont, bg="#5454c5", fg="#342056",activeforeground="#342056",activebackground="#639cd9",command=anaekrandon).place(relx=0.38, rely=0.9)


def hepsineyukle():
    global dizin
    global muzik_dosya_yolu
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    pygame.mixer.quit()

    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=(
        (".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//a"):
            dosyaYolu = os.path.join("Music Folder//a", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//a")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//b"):
            dosyaYolu = os.path.join("Music Folder//b", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//b")

    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//c"):
            dosyaYolu = os.path.join("Music Folder//c", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//c")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//d"):
            dosyaYolu = os.path.join("Music Folder//d", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//d")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//e"):
            dosyaYolu = os.path.join("Music Folder//e", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//e")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//f"):
            dosyaYolu = os.path.join("Music Folder//f", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//f")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//g"):
            dosyaYolu = os.path.join("Music Folder//g", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//g")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//h"):
            dosyaYolu = os.path.join("Music Folder//h", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//h")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//i"):
            dosyaYolu = os.path.join("Music Folder//i", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//i")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//j"):
            dosyaYolu = os.path.join("Music Folder//j", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//j")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//k"):
            dosyaYolu = os.path.join("Music Folder//k", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//k")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//l"):
            dosyaYolu = os.path.join("Music Folder//l", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//l")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//m"):
            dosyaYolu = os.path.join("Music Folder//m", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//m")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//n"):
            dosyaYolu = os.path.join("Music Folder//n", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//n")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//o"):
            dosyaYolu = os.path.join("Music Folder//o", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//o")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//p"):
            dosyaYolu = os.path.join("Music Folder//p", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//p")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//r"):
            dosyaYolu = os.path.join("Music Folder//r", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//r")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//s"):
            dosyaYolu = os.path.join("Music Folder//s", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//s")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//t"):
            dosyaYolu = os.path.join("Music Folder//t", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//t")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//u"):
            dosyaYolu = os.path.join("Music Folder//u", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//u")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//v"):
            dosyaYolu = os.path.join("Music Folder//v", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//v")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//y"):
            dosyaYolu = os.path.join("Music Folder//y", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//y")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//z"):
            dosyaYolu = os.path.join("Music Folder//z", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//z")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//w"):
            dosyaYolu = os.path.join("Music Folder//w", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//w")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//x"):
            dosyaYolu = os.path.join("Music Folder//x", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//x")


    if uzanti == ".mp3":
        for dosya in os.listdir("Music Folder//q"):
            dosyaYolu = os.path.join("Music Folder//q", dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, "Music Folder//q")
        print("Tüm Klasörlere Kopyalandı")




def hepsinisil():
    pygame.mixer.quit()

    for dosya in os.listdir("Music Folder//a"):
        dosyaYolu = os.path.join("Music Folder//a", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//b"):
        dosyaYolu = os.path.join("Music Folder//b", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//c"):
        dosyaYolu = os.path.join("Music Folder//c", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//d"):
        dosyaYolu = os.path.join("Music Folder//d", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//e"):
        dosyaYolu = os.path.join("Music Folder//e", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//f"):
        dosyaYolu = os.path.join("Music Folder//f", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//g"):
        dosyaYolu = os.path.join("Music Folder//g", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//h"):
        dosyaYolu = os.path.join("Music Folder//h", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//i"):
        dosyaYolu = os.path.join("Music Folder//i", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//j"):
        dosyaYolu = os.path.join("Music Folder//j", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//k"):
        dosyaYolu = os.path.join("Music Folder//k", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//l"):
        dosyaYolu = os.path.join("Music Folder//l", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//m"):
        dosyaYolu = os.path.join("Music Folder//m", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//n"):
        dosyaYolu = os.path.join("Music Folder//n", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//o"):
        dosyaYolu = os.path.join("Music Folder//o", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//p"):
        dosyaYolu = os.path.join("Music Folder//p", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//r"):
        dosyaYolu = os.path.join("Music Folder//r", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//s"):
        dosyaYolu = os.path.join("Music Folder//s", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//t"):
        dosyaYolu = os.path.join("Music Folder//t", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//u"):
        dosyaYolu = os.path.join("Music Folder//u", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//v"):
        dosyaYolu = os.path.join("Music Folder//v", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//y"):
        dosyaYolu = os.path.join("Music Folder//y", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//z"):
        dosyaYolu = os.path.join("Music Folder//z", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//w"):
        dosyaYolu = os.path.join("Music Folder//w", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//x"):
        dosyaYolu = os.path.join("Music Folder//x", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)

    for dosya in os.listdir("Music Folder//q"):
        dosyaYolu = os.path.join("Music Folder//q", dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
            elif os.path.isdir(dosyaYolu):
                shutil.rmtree(dosyaYolu, ignore_errors=True)
        except Exception as hata:
            print(hata)
            messagebox.showinfo("Hata", hata)



def harfmuzik_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    pygame.mixer.quit()


    if uzanti == ".mp3":
        for dosya in os.listdir(dizin):
            dosyaYolu = os.path.join(dizin, dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu, ignore_errors=True)
            except Exception as hata:
                print(hata)
                messagebox.showinfo("Hata", hata)
        shutil.copy(muzik_dosya_yolu, dizin)
        print("Kopyalandı")

        anaekrandon()
    #if uzanti != ".mp3":
        #messagebox.showinfo("Hata", "Yalnızca mp3 Uzantılı Dosya Ekleyebilirsin.")



def a_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//a'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def b_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//b'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def c_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//c'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def d_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//d'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def e_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//e'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def f_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//f'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def g_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//g'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def h_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//h'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def i_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//i'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def j_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//j'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def k_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//k'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def l_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//l'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def m_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//m'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def n_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//n'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def o_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//o'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def p_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//p'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def q_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//q'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def r_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//r'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def s_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//s'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def t_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//t'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def u_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//u'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def v_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//v'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def w_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//w'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def w_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//w'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def x_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//x'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def y_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//y'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()


def z_harfdizin_belirle():
    global dizin
    global muzik_dosya_yolu
    global filename
    global dosya
    global uzanti
    dizin = 'Music Folder//z'
    muzik_dosya_yolu = filedialog.askopenfilename(title="Müzik Dosyasını Seç", filetypes=((".mp3 uzantılı dosyalar", "*.mp3"), ("Tüm dosyalar", "*.*")))
    filename = os.path.basename(muzik_dosya_yolu)
    dosya = os.path.splitext(filename)
    uzanti = dosya[1]
    harfmuzik_belirle()











def listenerthreading():

    def on_press(key):
        print(key)

        if str(key) == "'a'":
            if harf_a.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//a")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//a//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()


        if str(key) == "'b'":
            if harf_b.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//b")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//b//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()


        if str(key) == "'c'":
            if harf_c.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//c")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//c//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()


        if str(key) == "'d'":
            if harf_d.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//d")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//d//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()


        if str(key) == "'e'":
            if harf_e.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//e")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//e//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()


        if str(key) == "'f'":
            if harf_f.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//f")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//f//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'g'":
            if harf_g.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//g")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//g//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'h'":
            if harf_h.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//h")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//h//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'i'":
            if harf_i.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//i")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//i//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'j'":
            if harf_j.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//j")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//j//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'k'":
            if harf_k.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//k")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//k//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'l'":
            if harf_l.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//l")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//l//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'m'":
            if harf_m.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//m")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//m//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'n'":
            if harf_n.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//n")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//n//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'o'":
            if harf_o.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//o")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//o//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'p'":
            if harf_p.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//p")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//p//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'r'":
            if harf_r.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//r")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//r//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'s'":
            if harf_s.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//s")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//s//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()


        if str(key) == "'t'":
            if harf_t.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//t")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//t//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'u'":
            if harf_u.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//u")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//u//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()


        if str(key) == "'v'":
            if harf_v.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//v")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//v//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'y'":
            if harf_y.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//y")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//y//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'z'":
            if harf_z.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//z")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//z//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'w'":
            if harf_w.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//w")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//w//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'x'":
            if harf_x.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//x")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//x//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()



        if str(key) == "'q'":
            if harf_q.get() == 0:
                print("Harf işaretli değil")
            else:
                tarama = os.scandir("Music Folder//q")
                for belge in tarama:
                    dosya = belge.name
                    mscdosya = "Music Folder//q//" + dosya
                    print(mscdosya)
                    pygame.mixer.init()
                    pygame.mixer.music.load(mscdosya)
                    pygame.mixer.music.play()


    with Listener(on_press=on_press) as listener:
        listener.join()



listenerrthread = threading.Thread(target=listenerthreading)
listenerrthread.start()



muzikbaslikfont = font.Font(size="20", underline=1)
muzikbaslik = Label(muzikayarekran, text="Müzik Ayarları", bg="#5454c5", fg="#342056", font=muzikbaslikfont).place(relx="0.35", rely="0.01")


a_harfbtnfont = font.Font(size="12")
a_harfbtn = Button(muzikayarekran, text="A Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=a_harfbtnfont, command=a_harfdizin_belirle).place(relx=0.10,rely=0.15)

b_harfbtnfont = font.Font(size="12")
b_harfbtn = Button(muzikayarekran, text="B Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=b_harfdizin_belirle).place(relx=0.10,rely=0.25)

c_harfbtnfont = font.Font(size="12")
c_harfbtn = Button(muzikayarekran, text="C Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=c_harfdizin_belirle).place(relx=0.10,rely=0.35)

d_harfbtnfont = font.Font(size="12")
d_harfbtn = Button(muzikayarekran, text="D Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=d_harfdizin_belirle).place(relx=0.10,rely=0.45)

e_harfbtnfont = font.Font(size="12")
e_harfbtn = Button(muzikayarekran, text="E Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=e_harfdizin_belirle).place(relx=0.10,rely=0.55)

f_harfbtnfont = font.Font(size="12")
f_harfbtn = Button(muzikayarekran, text="F Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=f_harfdizin_belirle).place(relx=0.10,rely=0.65)

g_harfbtnfont = font.Font(size="12")
g_harfbtn = Button(muzikayarekran, text="G Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=g_harfdizin_belirle).place(relx=0.10,rely=0.75)

h_harfbtnfont = font.Font(size="12")
h_harfbtn = Button(muzikayarekran, text="H Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=h_harfdizin_belirle).place(relx=0.30,rely=0.15)

i_harfbtnfont = font.Font(size="12")
i_harfbtn = Button(muzikayarekran, text="i Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=i_harfdizin_belirle).place(relx=0.30,rely=0.25)

j_harfbtnfont = font.Font(size="12")
j_harfbtn = Button(muzikayarekran, text="J Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=j_harfdizin_belirle).place(relx=0.30,rely=0.35)

k_harfbtnfont = font.Font(size="12")
k_harfbtn = Button(muzikayarekran, text="K Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=k_harfdizin_belirle).place(relx=0.30,rely=0.45)

l_harfbtnfont = font.Font(size="12")
l_harfbtn = Button(muzikayarekran, text="L Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=l_harfdizin_belirle).place(relx=0.30,rely=0.55)

m_harfbtnfont = font.Font(size="12")
m_harfbtn = Button(muzikayarekran, text="M Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=m_harfdizin_belirle).place(relx=0.30,rely=0.65)

n_harfbtnfont = font.Font(size="12")
n_harfbtn = Button(muzikayarekran, text="N Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=n_harfdizin_belirle).place(relx=0.30,rely=0.75)

o_harfbtnfont = font.Font(size="12")
o_harfbtn = Button(muzikayarekran, text="O Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=o_harfdizin_belirle).place(relx=0.60,rely=0.15)

p_harfbtnfont = font.Font(size="12")
p_harfbtn = Button(muzikayarekran, text="P Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=p_harfdizin_belirle).place(relx=0.60,rely=0.25)

r_harfbtnfont = font.Font(size="12")
r_harfbtn = Button(muzikayarekran, text="R Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=r_harfdizin_belirle).place(relx=0.60,rely=0.35)

s_harfbtnfont = font.Font(size="12")
s_harfbtn = Button(muzikayarekran, text="S Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=s_harfdizin_belirle).place(relx=0.60,rely=0.45)

t_harfbtnfont = font.Font(size="12")
t_harfbtn = Button(muzikayarekran, text="T Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=t_harfdizin_belirle).place(relx=0.60,rely=0.55)

u_harfbtnfont = font.Font(size="12")
u_harfbtn = Button(muzikayarekran, text="U Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=u_harfdizin_belirle).place(relx=0.60,rely=0.65)

v_harfbtnfont = font.Font(size="12")
v_harfbtn = Button(muzikayarekran, text="V Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=v_harfdizin_belirle).place(relx=0.60,rely=0.75)

y_harfbtnfont = font.Font(size="12")
y_harfbtn = Button(muzikayarekran, text="Y Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=y_harfdizin_belirle).place(relx=0.80,rely=0.15)

z_harfbtnfont = font.Font(size="12")
z_harfbtn = Button(muzikayarekran, text="Z Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=z_harfdizin_belirle).place(relx=0.80,rely=0.25)

w_harfbtnfont = font.Font(size="12")
w_harfbtn = Button(muzikayarekran, text="W Harfi", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=w_harfdizin_belirle).place(relx=0.80,rely=0.35)

x_harfbtnfont = font.Font(size="12")
x_harfbtn = Button(muzikayarekran, text="X Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=x_harfdizin_belirle).place(relx=0.80,rely=0.45)

q_harfbtnfont = font.Font(size="12")
q_harfbtn = Button(muzikayarekran, text="Q Harfi ", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=b_harfbtnfont, command=q_harfdizin_belirle).place(relx=0.80,rely=0.55)

hepsineyuklefnt = font.Font(size="10")
hepsineyuklebtn = Button(muzikayarekran, text="Hepsine Yükle", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=hepsineyuklefnt, command=hepsineyukle).place(relx=0.80,rely=0.65)

hepsinisilfnt = font.Font(size="10")
hepsinisilebtn = Button(muzikayarekran, text="Hepsini Sil", bg="#5454c5", fg="#342056", activeforeground="#342056", activebackground="#639cd9", font=hepsinisilfnt, command=hepsinisil).place(relx=0.80,rely=0.75)


gerifont = font.Font(size="15")
geri = Button(muzikayarekran, text="Geri", bg="#5454c5", fg="#342056", activeforeground="#342056",activebackground="#639cd9", font=gerifont, command=anaekrandon).place(relx=0.46, rely=0.87)


def on_closing():
    window.destroy()
    pygame.mixer.quit()


window.protocol("WM_DELETE_WINDOW", on_closing)



show_frame(anaekran)
window.mainloop()