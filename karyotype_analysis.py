
import os
from aixplain.factories import AgentFactory
from aixplain.modules.agent import ModelTool

# Configurar a chave de API

def create_karyotype_agent():
    # Criar um agente para análise de cariótipos
    agent = AgentFactory.create(
        name="Karyotype Analysis Agent",
        description="You are an agent that analyzes karyotype images and provides insights.",
        tools=[
            # Usar um modelo de visão computacional genérico
            ModelTool(model="65c51c556eb563350f6e1bb1"),  # Este é um ID de modelo genérico, pode precisar ser alterado
        ],
    )
    return agent

def analyze_karyotype(agent, image_path):
    # Analisar uma imagem de cariótipo
    with open(image_path, "rb") as image_file:
        response = agent.run(f"Analyze this karyotype image and provide insights: {image_file.read()}")
    return response

if __name__ == "__main__":
    agent = create_karyotype_agent()
    # Exemplo de uso (substitua 'path_to_image.jpg' pelo caminho real da imagem)
    result = analyze_karyotype(agent, 'path_to_image.jpg')
    print(result)
