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
		<li><code>cv2</code>: Biblioteca OpenCV, que fornece funções para processamento de imagens e visão computacional.</li>
		<li><code>tkinter</code>: Biblioteca Tkinter, que fornece uma interface gráfica para Python.</li>
		<li><code>filedialog</code>: Módulo da biblioteca Tkinter que permite selecionar arquivos do sistema de arquivos.</li>
		<li><code>Image</code>: Módulo da biblioteca PIL que permite trabalhar com imagens.</li>
		<li><code>ImageTk</code>: Módulo da biblioteca PIL que permite converter imagens para o formato PhotoImage, que pode ser usado no canvas do Tkinter.</li>
	</ul>
</table>

## Classe VisaoComputacionalApp

A classe <b>VisaoComputacional</b> é a <i>classe principal</i> da aplicação. Ela contém os seguintes métodos:

<table>
	<ul>
		<li><code>__init__(self, root)</code>: Método construtor da classe. Inicializa os componentes da interface gráfica e define o modelo de visão computacional.</li>
		<li><code>carregar_imagem(self)</code>: Método que carrega uma imagem do sistema de arquivos.</li>
		<li><code>iniciar_webcam(self)</code>: Método que inicia a webcam.</li>
		<li><code>processar_imagem(self, imagem)</code>: Método que processa uma imagem usando o modelo de visão computacional.</li>
		<li><code>mostrar_resultado(self, resultado)</code>: Método que exibe o resultado do processamento da imagem.</li>
	</ul>
</table>

## Método init(self, root)

O método construtor da classe <b>VisaoComputacional</b> inicia os seguintes componentes da <i>interface gráfica</i>:

<table>
	<ul>
		<li>Um botão para carregar uma imagem.</li>
		<li>Um botão para iniciar a webcam.</li>
		<li>Uma etiqueta para exibir o resultado do processamento da imagem.</li>
		<li>Um <a href="https://github.com/leostella97/detecta_objetos#d%C3%BAvidas">canvas (?)</a> para exibir a imagem processada.</li>
	</ul>
</table>

## Teste de detecção de rosto
<img src="https://github.com/leostella97/detecta_objetos/blob/main/img/rosto_detectado.png?raw=true">

## Dúvidas
• <b>Canvas</b> é uma matriz bidimensional de pixels, que podem ser usados para representar imagens, gráficos e texto.<br>Ele também pode ser usado para armazenar dados de outras formas, como pontos, linhas e formas.