import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class VisaoComputacionalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visão Computacional")

        self.botao_enviar_foto = tk.Button(root, text="ENVIAR FOTO", command=self.carregar_imagem)
        self.botao_enviar_foto.pack()

        self.botao_iniciar_webcam = tk.Button(root, text="INICIAR WEBCAM", command=self.iniciar_webcam)
        self.botao_iniciar_webcam.pack()

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

    def carregar_imagem(self):
        path = filedialog.askopenfilename()
        imagem = cv2.imread(path)
        resultado = self.processar_imagem(imagem)
        self.mostrar_resultado(resultado)

    def iniciar_webcam(self):
        captura = cv2.VideoCapture(0)
        while True:
            ret, frame = captura.read()
            resultado = self.processar_imagem(frame)
            self.mostrar_resultado(resultado)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        captura.release()
        cv2.destroyAllWindows()

    def processar_imagem(self, imagem):
        # Lógica de processamento de imagem (classificação de objetos, por exemplo) aqui
        # Substitua esta lógica pelo seu modelo de visão computacional

        # Exemplo: detecção de rosto usando o classificador Haarcascades
        classificador = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        objetos = classificador.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in objetos:
            cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(imagem, "Rosto", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        return imagem

    def mostrar_resultado(self, resultado):
        resultado = cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB)
        imagem = Image.fromarray(resultado)
        imagem = ImageTk.PhotoImage(imagem)

        # Atualizar a imagem no canvas
        self.canvas.config(width=imagem.width(), height=imagem.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=imagem)
        self.root.update_idletasks()  # Atualizar a interface gráfica

if __name__ == "__main__":
    root = tk.Tk()
    app = VisaoComputacionalApp(root)
    root.mainloop()
