# Detector de objetos em Python
## Bibliotecas usadas
<table>
	<ul>
		<li>tkinter</li>
		<li>cv2</li>
		<li>PIL</li>
	</ul>
</table>

## Sobre o código
Aplicação simples de <code>visão computacional</code> em Python. Ele permite <b>carregar uma imagem</b> ou <b>iniciar a webcam</b>, e então processa a imagem usando um modelo de visão computacional. O resultado do processamento é exibido em um canvas.

## Começo do código
O código começa importando as seguintes bibliotecas:
<br>
<table>
	<ul>
		<li><code>cv2</code></li>: Biblioteca OpenCV, que fornece funções para processamento de imagens e visão computacional.
		<li><code>tkinter</code></li>: Biblioteca Tkinter, que fornece uma interface gráfica para Python.
		<li><code>filedialog</code></li>: Módulo da biblioteca Tkinter que permite selecionar arquivos do sistema de arquivos.
		<li><code>Image</code></li>: Módulo da biblioteca PIL que permite trabalhar com imagens.
		<li><code>ImageTk</code></li>: Módulo da biblioteca PIL que permite converter imagens para o formato PhotoImage, que pode ser usado no canvas do Tkinter.
	</ul>
</table>


Teste de detecção de rosto
<img src="https://github.com/leostella97/detecta_objetos/blob/main/img/rosto_detectado.png?raw=true">

## Dúvidas
• <b>Canvas</b> é uma matriz bidimensional de pixels, que podem ser usados para representar imagens, gráficos e texto.<br>Ele também pode ser usado para armazenar dados de outras formas, como pontos, linhas e formas.