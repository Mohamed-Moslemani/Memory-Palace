from app.retrieval import retrieve_ideas, retrieve_passwords
from app.llama_model import generate_response_llama

def process_user_query(user_id, query, query_type):
    """
    Process the user's query using retrieval and LLaMA.
    - query_type: 'idea' or 'password'
    """
    if query_type == "idea":
        retrieved_ideas = retrieve_ideas(user_id, query)
        if not retrieved_ideas:
            return "I couldn't find any ideas matching your query."

        context = "\n".join([f"- {idea['idea']}" for idea in retrieved_ideas])
        prompt = f"""
        User Query: "{query}"

        Relevant Ideas:
        {context}

        Provide a response based on these ideas.
        """
        return generate_response_llama(prompt)

    elif query_type == "password":
        retrieved_passwords = retrieve_passwords(user_id, query)
        if not retrieved_passwords:
            return "I couldn't find any passwords matching your query."

        context = "\n".join([f"{pw['service']}: {pw['password']}" for pw in retrieved_passwords])
        prompt = f"""
        User Query: "{query}"

        Relevant Passwords:
        {context}

        Provide a response based on these passwords.
        """
        return generate_response_llama(prompt)

    return "Invalid query type."
