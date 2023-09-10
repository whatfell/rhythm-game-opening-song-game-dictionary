import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

class Dictionary:
    def __init__(self):
        self.word_list = {}

        # 初始化词库
        self.add_word("Glaciaxion", "Phigros")
        self.add_word("Eradication Catastrophe", "Phigros")
        self.add_word("Credits", "Phigros")
        self.add_word("Dlyrotz", "Phigros")
        self.add_word("Engine x Start!! (melody mix)", "Phigros")
        self.add_word("光", "Phigros")
        self.add_word("Winter↑cube↓", "Phigros")
        self.add_word("混乱-Confusion", "Phigros")
        self.add_word("Cipher : /2&//<|0", "Phigros")
        self.add_word("FULi AUTO SHOOTER", "Phigros")
        self.add_word("HumaN", "Phigros")
        self.add_word("[PRAW]", "Phigros")
        self.add_word("Cereris", "Phigros")
        self.add_word("Pixel Rebelz", "Phigros")
        self.add_word("Non-Melodic Ragez(MUG Edit)", "Phigros")
        self.add_word("Sultan Rage", "Phigros")
        self.add_word("-SURREALISM-", "Phigros")
        self.add_word("Bonus Time", "Phigros")
        self.add_word("ENERGY SYNERGY MATRIX", "Phigros")
        self.add_word("NYA!!!(Phigros ver.)", "Phigros")
        self.add_word("JunXion Between Life And Death(VIP Mix)", "Phigros")
        self.add_word("cryout", "Phigros")
        self.add_word("Reimei", "Phigros")
        self.add_word("尊師 ～The Guru～", "Phigros")
        self.add_word("Spasmodic", "Phigros")
        self.add_word("Leave All Behind", "Phigros")
        self.add_word("Colorful Days♪", "Phigros")
        self.add_word("micro.wav", "Phigros")
        self.add_word("重生", "Phigros")
        self.add_word("NO ONE YES MAN", "Phigros")
        self.add_word("望影の方舟Six", "Phigros")
        self.add_word("Igallta", "Phigros")
        self.add_word("Clock Paradox", "Phigros")
        self.add_word("Chronologika", "Phigros")
        self.add_word("Nick of Time", "Phigros")
        self.add_word("Chronomia", "Phigros")
        self.add_word("Chronos Collapse - La Campanella", "Phigros")
        self.add_word("Rrhar'il", "Phigros")
        self.add_word("Crave Wave", "Phigros")
        self.add_word("The Chariot ~REVIIVAL~", "Phigros")
        self.add_word("Luminescence", "Phigros")
        self.add_word("Retribution", "Phigros")
        self.add_word("DESTRUCTION 3,2,1", "Phigros")
        self.add_word("Distorted Fate", "Phigros")
        self.add_word("Ποσειδών", "Phigros")
        self.add_word("WATER", "Phigros")
        self.add_word("Miracle Forest (VIP Mix)", "Phigros")
        self.add_word("MOBILYS", "Phigros")
        self.add_word("Lyrith -迷宮リリス-", "Phigros")
        self.add_word("Demiurge", "Phigros")
        self.add_word("Demonkin", "Phigros")
        self.add_word("Re_Nascence (Psystyle Ver.)", "Phigros")
        self.add_word("Ark", "Phigros")
        self.add_word("After Dawn", "Phigros")
        self.add_word("INFiNiTE ENERZY -Overdoze-", "Phigros")
        self.add_word("Another Me(Neutral Moon)", "Phigros")
        self.add_word("mechanted", "Phigros")
        self.add_word("life flashes before weeb eyes", "Phigros")
        self.add_word("Break Through The Barrier", "Phigros")
        self.add_word("Chronostasis[Phi]", "Phigros")
        self.add_word("Infinity Heaven", "Phigros")
        self.add_word("Disorder", "Phigros")
        self.add_word("CROSS†SOUL", "Phigros")
        self.add_word("GOODTEK", "Phigros")
        self.add_word("GOODBOUNCE", "Phigros")
        self.add_word("GOODWORLD", "Phigros")
        self.add_word("GOODFORTUNE", "Phigros")
        self.add_word("GOODRAGE", "Phigros")
        self.add_word("Initialize", "Phigros")
        self.add_word("桜樹街道", "Phigros")
        self.add_word("Get Ready!!", "Phigros")
        self.add_word("volcanic", "Phigros")
        self.add_word("XING", "Phigros")
        self.add_word("Final Step!", "Phigros")
        self.add_word("Time to Night Sky (feat. Lee Yu Jin)", "Phigros")
        self.add_word("HAZARD", "Phigros")
        self.add_word("Another Me(D_AAN)", "Phigros")
        self.add_word("Don't Never Around", "Phigros")
        self.add_word("RESSiSTANCE", "Phigros")
        self.add_word("Apocalypse", "Phigros")
        self.add_word("Protoflicker", "Phigros")
        self.add_word("Horizon Blue", "Phigros")
        self.add_word("You are the Miserable", "Phigros")
        self.add_word("Stasis", "Phigros")
        self.add_word("Shadow", "Phigros")
        self.add_word("心之所向", "Phigros")
        self.add_word("inferior", "Phigros")
        self.add_word("盏茗", "Phigros")
        self.add_word("青芽", "Phigros")
        self.add_word("瓷岁", "Phigros")
        self.add_word("Feast远东之宴", "Phigros")
        self.add_word("神話", "Phigros")
        self.add_word("El último baile", "Phigros")
        self.add_word("Trojan", "Phigros")
        self.add_word("Temporal Shifting", "Phigros")
        self.add_word("Ad astra per aspera", "Phigros")
        self.add_word("A journey to the moonlight", "Phigros")
        self.add_word("Doppelganger", "Phigros")
        self.add_word("もぺもぺ(Phi)", "Phigros")
        self.add_word("MARENOL", "Phigros")
        self.add_word("萤火虫の怨", "Phigros")
        self.add_word("万吨匿名信", "Phigros")
        self.add_word("风屿", "Phigros")
        self.add_word("dB doll", "Phigros")
        self.add_word("Dash", "Phigros")
        self.add_word("云女孩", "Phigros")
        self.add_word("Drop It", "Phigros")
        self.add_word("RIPPER", "Phigros")
        self.add_word("Drop It", "Phigros")
        self.add_word("Aphasia", "Phigros")
        self.add_word("开心病", "Phigros")
        self.add_word("華灯爱", "Phigros")
        self.add_word("Find_Me", "Phigros")
        self.add_word("Sein", "Phigros")
        self.add_word("狂喜蘭舞", "Phigros")
        self.add_word("Sparkle New Life", "Phigros")
        self.add_word("Khronostasis Katharsis", "Phigros")
        self.add_word("Snow Desert", "Phigros")
        self.add_word("Burn", "Phigros")
        self.add_word("Aleph-0", "Phigros")
        self.add_word("Next Time", "Phigros")
        self.add_word("Rubbish Sorting", "Phigros")
        self.add_word("Dead Soul", "Phigros")
        self.add_word("Speed Up!", "Phigros")
        self.add_word("Magenta Potion", "Phigros")
        self.add_word("Get Back", "Phigros")
        self.add_word("Palescreen", "Phigros")
        self.add_word("The Mountain Eater", "Phigros")
        self.add_word("Orthodox", "Phigros")
        self.add_word("End Me", "Phigros")
        self.add_word("Parallel Retrogression (Game Ver.)", "Phigros")
        self.add_word("Starduster", "Phigros")
        self.add_word("Electron", "Phigros")
        self.add_word("SIGMA", "Phigros")
        self.add_word("Hardcore Kwaya", "Phigros")
        self.add_word("Äventyr", "Phigros")
        self.add_word("Träne", "Phigros")
        self.add_word("雪降り、メリクリ", "Phigros")
        self.add_word("Cervelle Connexion", "Phigros")
        self.add_word("modulus", "Phigros")
        self.add_word("Wavetapper", "Phigros")
        self.add_word("大和撫子 -Wild Dances-", "Phigros")
        self.add_word("Eltaw", "Phigros")
        self.add_word("Better Graphic Animation", "Phigros")
        self.add_word("With You", "Phigros")
        self.add_word("Unorthodox Thoughts", "Phigros")
        self.add_word("Apocalyptic", "Phigros")
        self.add_word("游园地", "Phigros")
        self.add_word("energy trixxx", "Phigros")
        self.add_word("Nhelv", "Phigros")
        self.add_word("-Arkhei-", "Phigros")
        self.add_word("Kerberos", "Phigros")
        self.add_word("ρars/ey", "Phigros")
        self.add_word("Concvssion", "Phigros")
        self.add_word("ジングルベル(Jingle Bell)", "Phigros")
        self.add_word("Dreamland", "Phigros")
        self.add_word("Another Round", "Phigros")
        self.add_word("996", "Phigros")
        self.add_word("Future Mind", "Phigros")
        self.add_word("Luminescent", "Phigros")
        self.add_word("FULi AUTO BUSTER", "Phigros")
        self.add_word("I Must Say No", "Phigros")
        self.add_word("opia", "Phigros")
        self.add_word("いざ、参ります", "Phigros")
        self.add_word("月下缭乱", "Phigros")
        self.add_word("On And On!!", "Phigros")
        self.add_word("DataErr0r", "Phigros")
        self.add_word("c.s.q.n.", "Phigros")
        self.add_word("Brave Notes", "Phigros")
        self.add_word("Eternal Snow", "Phigros")
        self.add_word("Rainy Season", "Phigros")
        self.add_word("El Condor Pasa (Phigros Edit)", "Phigros")
        self.add_word("Break Over", "Phigros")
        self.add_word("Believe Light (feat. 果丸哒呦)", "Phigros")
        self.add_word("Pont des souvenirs", "Phigros")
        self.add_word("青丘", "Phigros")
        self.add_word("インフェルノシティ", "Phigros")
        self.add_word("Upshift", "Phigros")
        self.add_word("Poison AND÷OR Affection", "Phigros")
        self.add_word("Random", "Phigros")
        self.add_word("零號車輛", "Phigros")
        self.add_word("Bougainvillea", "Phigros")
        self.add_word("Now Is The Time, Do It", "Phigros")
        self.add_word("Rainy Heart", "Phigros")
        self.add_word("Realms", "Phigros")
        self.add_word("ぱぴぷぴぷぴぱ(pa pi pu pi pu pi pa)", "Phigros")
        self.add_word("Triumph & Regret", "Phigros")
        self.add_word("S.A.T.E.L.L.I.T.E.", "Phigros")
        self.add_word("Dance with Silence", "Phigros")
        self.add_word("Labyrinth in Kowloon: Walled World", "Phigros")
        self.add_word("Compute It With Some Devilish Alcoholic Steampunk Engines", "Phigros")
        self.add_word("+ERABY+E CONNEC+10N", "Phigros")

    def add_word(self, word, definition):
        self.word_list[word] = definition

    def search_word(self, keyword):
        results = []
        for word, definition in self.word_list.items():
            if keyword.lower() in word.lower():
                results.append((word, definition))
        return results

class DictionaryGUI:
    def __init__(self, root):
        self.dictionary = Dictionary()
        self.root = root
        self.root.title("Rhythm-Game-Opening-Song-Game-Dictionary By Tr4sH")

        self.search_label = tk.Label(self.root, text="请输入要搜索的关键字：", font=("微软雅黑", 20))
        self.search_label.pack()

        self.search_entry = tk.Entry(self.root, font=("微软雅黑", 20))
        self.search_entry.pack()
        self.search_entry.bind("<Return>", self.search_word)

        self.search_button = tk.Button(self.root, text="搜索", font=("微软雅黑", 20), command=self.search_word)
        self.search_button.pack()

        self.search_results_text = scrolledtext.ScrolledText(self.root, font=("微软雅黑", 20), width=40, height=25)
        self.search_results_text.pack()

        self.root.geometry("828x1092")

    def search_word(self, event=None):
        keyword = self.search_entry.get()
        results = self.dictionary.search_word(keyword)

        if results:
            result_text = "搜索结果：\n"
            for word, definition in results:
                result_text += f"{word}: {definition}\n"
            self.search_results_text.delete(1.0, tk.END)
            self.search_results_text.insert(tk.END, result_text)
        else:
            messagebox.showinfo("结果", "未找到匹配的单词。")

root = tk.Tk()
dictionary_gui = DictionaryGUI(root)
root.mainloop()
