from swarm import Swarm, Agent

client = Swarm()

def transfer_to_agent_b(id = None):
    print(f"Transferring to Agent B")
    print(f"ID: {id}")
    return agent_b


prompt1 = "Hi"
prompt2 = "What is the capital of France?"

agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
    model="llama3.2",
)

agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
    model="llama3.2",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": prompt2}],
)

#print(response.messages[-1]["content"])
print(response.agent)