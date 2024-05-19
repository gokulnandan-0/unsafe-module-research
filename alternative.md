## Unsafe module detection using LLM

The documentation along with code files can be passed to any LLM to point out the unsafe module. however, this methods has the following issues:
*   **Context Limit :** The context limit of such an input would be very high, causing for partial or broken content.
*   **Hallucination :** The High and repetetive content in such inputs generally causes the LLM to hallucinate, making the generated outputs to be futile.

### Solution:

The most direct method one can use to define such an LLM based module detection would be then to create a RAG based LLM product. 

RAG or Retrieval Augmented Generation is an updated method in which an LLM can be used to generate inpput customed content by passing additional content along with the questions to increase the generation ability. 
#### Product idea:

1. The static analyis tools along with simple ast based redirection can be used to go to each function in a code line.

2. Everytime the code redirects to any new function, a simple matching based algorithm like : *BM25*, *phrase embedding match* can be used to find the code definition from source code. (*This can also be done using function definition extraction*)
3. The call graph from code along with documentation from matching can be passed to the LLM along with some examples for few-shot learning( *Optional*) to point out unsafe modules.

This is an approach that can be implemented, if needed, for a more in-depth method segregation