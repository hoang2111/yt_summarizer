import sys
import tkinter as tk
from summarize import summarizer


def main():
    root = tk.Tk()
    root.title("YouTube Video Summarizer")

    label = tk.Label(root, text="Input YouTube Link:")
    input_entry = tk.Entry(root, fg="black", width=50)

    title_label = tk.Label(root, text="Video Title (optional):")
    title_entry = tk.Entry(root, fg="black", width=50)

    output_entry = tk.Text(root, fg="black", width=60, wrap="word")
    label.pack()
    input_entry.pack()

    title_label.pack()
    title_entry.pack()

    summarize_button = tk.Button(
        root,
        text="Summarize!",
        fg="black",
        command=lambda: summarize_and_display(input_entry, output_entry, title_entry)
    )

    reset_button = tk.Button(
        root,
        text="Reset!",
        fg="black",
        command=lambda: reset(output_entry)
    )
    summarize_button.pack()
    output_entry.pack()
    reset_button.pack()

    # Start the GUI event loop
    root.mainloop()


def summarize_and_display(input_entry: tk.Entry, output_entry: tk.Text, title_entry: tk.Entry) -> None:
    video_url = input_entry.get()
    summarized_content = summarizer(video_url, title_entry.get())
    output_entry.insert(tk.END, summarized_content)


def reset(output_entry: tk.Text):
    output_entry.delete("1.0", tk.END)


if __name__ == "__main__":
    main()
