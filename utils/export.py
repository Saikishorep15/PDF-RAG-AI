from datetime import datetime


def export_as_txt(messages):
    """
    Export chat as plain text.
    """

    content = []

    content.append("PDF RAG AI Assistant")
    content.append("=" * 50)
    content.append(
        f"Exported: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )
    content.append("")

    for message in messages:

        role = message["role"].capitalize()

        content.append(f"{role}:")

        content.append(message["content"])

        content.append("")

    return "\n".join(content)


def export_as_markdown(messages):
    """
    Export chat as Markdown.
    """

    md = []

    md.append("# PDF RAG AI Assistant Chat")
    md.append("")
    md.append(
        f"**Exported:** {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )
    md.append("")

    for message in messages:

        if message["role"] == "user":

            md.append("## 👤 User")

        else:

            md.append("## 🤖 Assistant")

        md.append("")

        md.append(message["content"])

        md.append("")

    return "\n".join(md)