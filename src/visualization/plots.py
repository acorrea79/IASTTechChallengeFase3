import matplotlib.pyplot as plt

def save_shap_bar(shap_df, output_path, top_n=15):
    data = shap_df.head(top_n).sort_values("mean_abs_shap")

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(data["variavel_base"], data["mean_abs_shap"])
    ax.set_xlabel("Média de abs(SHAP)")
    ax.set_title("Influência preditiva global")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
