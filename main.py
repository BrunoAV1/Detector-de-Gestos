import cv2
import mediapipe as mp

# Inicializando MediaPipe para detecção de mãos
mp_hands = mp.solutions.hands  # Solução de detecção de mãos
mp_drawing = mp.solutions.drawing_utils  # Utilitários para desenhar landmarks e conexões

# Função para identificar os gestos com base nas landmarks da mão
def reconhecer_gesto(landmarks):
    """
    Identifica gestos específicos com base na posição das landmarks da mão.
    :param landmarks: Coordenadas das landmarks detectadas pela solução MediaPipe Hands.
    :return: Nome do gesto identificado, ou None se nenhum gesto for reconhecido.
    """
    # Sim (joinha para cima)
    if (landmarks[4].y < landmarks[3].y and  # Polegar para cima
        landmarks[8].y > landmarks[6].y and  # Indicador dobrado
        landmarks[12].y > landmarks[10].y and  # Médio dobrado
        landmarks[16].y > landmarks[14].y and  # Anelar dobrado
        landmarks[20].y > landmarks[18].y):  # Mindinho dobrado
        return "Sim"

    # Não (joinha para baixo)
    elif (landmarks[4].y > landmarks[3].y and  # Polegar para baixo
          landmarks[8].y > landmarks[6].y and  # Indicador dobrado
          landmarks[12].y > landmarks[10].y and  # Médio dobrado
          landmarks[16].y > landmarks[14].y and  # Anelar dobrado
          landmarks[20].y > landmarks[18].y):  # Mindinho dobrado
        return "Nao"

    # Paz e Amor (Indicador e Médio estendidos, outros dedos dobrados)
    elif (landmarks[8].y < landmarks[6].y and  # Indicador estendido
          landmarks[12].y < landmarks[10].y and  # Médio estendido
          landmarks[16].y > landmarks[14].y and  # Anelar dobrado
          landmarks[20].y > landmarks[18].y):  # Mindinho dobrado
        return "Paz e Amor"

    # Te Amo (Polegar, Indicador e Mindinho estendidos)
    elif (landmarks[4].y < landmarks[3].y and  # Polegar estendido
          landmarks[8].y < landmarks[6].y and  # Indicador estendido
          landmarks[20].y < landmarks[18].y and  # Mindinho estendido
          landmarks[12].y > landmarks[10].y and  # Médio dobrado
          landmarks[16].y > landmarks[14].y):  # Anelar dobrado
        return "Te Amo"

    # Ok (Polegar e Indicador formando um círculo, outros dedos estendidos)
    elif (abs(landmarks[4].x - landmarks[8].x) < 0.05 and  # Polegar e indicador próximos (círculo)
          abs(landmarks[4].y - landmarks[8].y) < 0.05 and
          landmarks[12].y < landmarks[10].y and  # Médio estendido
          landmarks[16].y < landmarks[14].y and  # Anelar estendido
          landmarks[20].y < landmarks[18].y):  # Mindinho estendido
        return "Ok"

    # Gesto obsceno (Dedo do meio estendido, outros dobrados)
    elif (landmarks[12].y < landmarks[10].y and  # Médio estendido
          landmarks[8].y > landmarks[6].y and  # Indicador dobrado
          landmarks[16].y > landmarks[14].y and  # Anelar dobrado
          landmarks[20].y > landmarks[18].y):  # Mindinho dobrado
        return "Gesto obsceno kk"

    return None  # Nenhum gesto reconhecido

# Configuração de captura de vídeo
cap = cv2.VideoCapture(0)

# Configurando o MediaPipe Hands para detecção de uma única mão com alta confiança
with mp_hands.Hands(static_image_mode=False,  # Detecta mãos em sequência contínua
                    max_num_hands=1,  # Número máximo de mãos detectadas
                    min_detection_confidence=0.7,  # Confiança mínima para detecção inicial
                    min_tracking_confidence=0.7) as hands:  # Confiança mínima para rastreamento
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Falha ao acessar a câmera.")
            break

        # Espelhar a imagem para criar um efeito de "espelho"
        frame = cv2.flip(frame, 1)

        # Convertendo a imagem para RGB (necessário para o MediaPipe)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image)  # Processar a imagem para detectar mãos

        # Convertendo de volta para BGR (necessário para exibição com OpenCV)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Verificar se landmarks foram detectadas
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Desenhar landmarks e conexões na imagem
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Reconhecer o gesto com base nas landmarks da mão
                gesto = reconhecer_gesto(hand_landmarks.landmark)
                if gesto:
                    # Determinar o retângulo em torno da mão
                    h, w, _ = image.shape
                    x_min = int(min([lm.x for lm in hand_landmarks.landmark]) * w)
                    y_min = int(min([lm.y for lm in hand_landmarks.landmark]) * h)
                    x_max = int(max([lm.x for lm in hand_landmarks.landmark]) * w)
                    y_max = int(max([lm.y for lm in hand_landmarks.landmark]) * h)

                    # Desenhar o retângulo em torno da mão
                    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 255, 0), 2)

                    # Exibir o nome do gesto na tela
                    cv2.putText(image, gesto, (x_min, y_min - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Exibir a imagem processada
        cv2.imshow('Reconhecimento de Gestos', image)

        # Pressione 'q' para sair do programa
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

# Liberar os recursos ao encerrar o programa
cap.release()
cv2.destroyAllWindows()
