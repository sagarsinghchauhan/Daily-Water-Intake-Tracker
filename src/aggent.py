import os 
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

meta_lamma_key = os.getenv('HUGGINGFACE_API_KEY')

llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Llama-3.1-8B-Instruct',
    task = 'text-generation',
    huggingfacehub_api_token=meta_lamma_key,
    temperature=0.5,
    max_new_tokens=256
)

model = ChatHuggingFace(llm = llm )

class WaterIntakeAgent:
    
    def __init__(self):
        self.history = []

    def analyze_intake(self,intake_ml):
        prompt = f"""
                you are a hydration assistant . the user has consumed{intake_ml} ml of water today.
                provide a hydration status suggest if they need to drink more water
                """
        
        response = model.invoke([HumanMessage(content = prompt)])
        return response.content

if __name__ == '__main__':
    agent = WaterIntakeAgent()
    intake= 500
    feedback = agent.analyze_intake(intake)
    print(f"hydration Analysis :{feedback}")
    



