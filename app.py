import gradio as gr
from codechecker import analyze_code
from specschecker import analyze_specs

def main():
    with gr.Blocks() as demo:
        gr.Markdown("# LLM Security Helper")
        gr.Markdown("Analyze code for vulnerabilities or map GenAI specs to OWASP/ATLAS frameworks.")

        with gr.Tabs():
            # Part 1: Code → Security Fixes
            with gr.TabItem("Part 1: Code Analysis"):
                gr.Markdown("### Input Vulnerable Code")
                code_input = gr.Textbox(
                    label="Code Snippet", 
                    placeholder="Paste your code here (e.g., Python, SQL, JS)...", 
                    lines=10
                )
                code_button = gr.Button("Scan for Vulnerabilities", variant="primary")
                code_output = gr.Markdown(label="Security Report")
                
                code_button.click(
                    fn=analyze_code, 
                    inputs=code_input, 
                    outputs=code_output
                )

            # Part 2: Specs → Vulnerabilities
            with gr.TabItem("Part 2: App Specs Analysis"):
                gr.Markdown("### Input GenAI App Specifications")
                spec_input = gr.Textbox(
                    label="App Specs", 
                    placeholder="Describe your Agentic app, its tools, and data access...", 
                    lines=10
                )
                spec_button = gr.Button("Map to OWASP & ATLAS", variant="primary")
                spec_output = gr.Markdown(label="Threat Model")
                
                spec_button.click(
                    fn=analyze_specs, 
                    inputs=spec_input, 
                    outputs=spec_output
                )

    demo.launch(share=True)

if __name__ == "__main__":
    main()