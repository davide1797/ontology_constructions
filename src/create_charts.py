import matplotlib.pyplot as plt
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from adjustText import adjust_text


def create_chart_automatic():
    # Data
    data_1 = [
        (1, "RELATION EXTRACTION", "DISTRIBUTIONAL SEMANTICS", "Casteleiro et al. (2016)"),
        (2, "RELATION EXTRACTION", "SPECIFIC", "Hamano et al. (2017)"),
        (3, "CONCEPT EXTRACTION", "CBOW", "Albukhitan et al. (2017)"),
        (4, "CONCEPT EXTRACTION", "SKIP-GRAM", "Albukhitan et al. (2017)"),
        (5, "TAXONOMY EXTRACTION", "CBOW", "Albukhitan et al. (2017)"),
        (6, "TAXONOMY EXTRACTION", "SKIP-GRAM", "Albukhitan et al. (2017)"),
        (7, "RELATION EXTRACTION", "SPECIFIC", "Cahyani et al. (2017)"),
        (8, "ONTOLOGY MATCHING", "SPECIFIC", "Cahyani et al. (2017)"),
        (9, "CONCEPT LEARNING", "SPECIFIC", "Mathews et al. (2017)"),
        (10, "TAXONOMY EXTRACTION", "SPECIFIC", "Mathews et al. (2017)"),
        (11, "RELATION EXTRACTION", "SPECIFIC", "Wang et al. (2017)"),
        (12, "RELATION EXTRACTION", "NLP PIPELINE", "Zhang et al. (2017)"),
        (13, "TAXONOMY EXTRACTION", "PATTERN MINING", "Potoniec et al. (2017)"),
        (14, "RELATION EXTRACTION", "NLP PIPELINE", "Albarghothi et al. (2018)"),
        (15, "ONTOLOGY MAPPING", "SPECIFIC", "Aggoune et al. (2018)"),
        (16, "RELATION EXTRACTION", "REGULAR EXPRESSIONS", "Kaushik et al. (2018)"),
        (17, "CONCEPT LEARNING", "RNN", "Petrucci et al. (2018)"),
        (18, "CONCEPT LEARNING", "ENCODER/DECODER", "Petrucci et al. (2018)"),
        (19, "CONCEPT EXTRACTION", "NLP PIPELINE", "Alobaidi et al. (2018)"),
        (20, "RELATION EXTRACTION", "NLP PIPELINE", "Alobaidi et al. (2018)"),
        (21, "ONTOLOGY MAPPING", "PATTERN MINING", "Deuna et al. (2018)"),
        (22, "ONTOLOGY MAPPING", "RULE-BASED", "Deuna et al. (2018)"),
        (23, "ONTOLOGY MAPPING", "RULE-BASED", "An et al. (2018)"),
        (24, "AXIOM LEARNING", "EMBEDDING", "Zhao et al. (2019)"),
        (25, "CONCEPT EXTRACTION", "CNN", "Capuano et al. (2020)"),
        (26, "CONCEPT LEARNING", "NLP PIPELINE", "Zaouga et al. (2021)"),
        (27, "RELATION EXTRACTION", "PATTERN MINING", "Zaouga et al. (2021)"),
        (28, "RULE LEARNING", "PATTERN MINING", "Zaouga et al. (2021)"),
        (29, "ONTOLOGY MAPPING", "SPECIFIC", "Ben et al. (2021)"),
        (30, "CONCEPT EXTRACTION", "LSTM", "Chen et al. (2021)"),
        (31, "RELATION EXTRACTION", "CNN", "Chen et al. (2021)"),
        (32, "ONTOLOGY MAPPING", "RULE-BASED", "Mhammedi et al. (2021)"),
        (33, "TERMS CLUSTERING", "LATENT DIRICHLET ANALYSIS", "Huang et al. (2021)"),
        (34, "RELATION EXTRACTION", "ATTENTION-BASED", "Heidari et al. (2021)"),
        (35, "ONTOLOGY MAPPING", "RULE-BASED", "Lakzaei et al. (2021)"),
        (36, "CONCEPT EXTRACTION", "NLP PIPELINE", "Meriah et al. (2021)"),
        (37, "AXIOM LEARNING", "EVOLUTIONARY ALGORITHM", "Felin et al. (2021)"),
        (38, "AXIOM LEARNING", "RULE-BASED", "Felin et al. (2021)"),
        (39, "RELATION EXTRACTION", "LATENT DIRICHLET ANALYSIS", "Xie et al. (2022)"),
        (40, "ONTOLOGY MAPPING", "RULE-BASED", "Leshcheva et al. (2022)"),
        (41, "CONCEPT EXTRACTION", "LATENT DIRICHLET ANALYSIS", "Tissaoui et al. (2022)"),
        (42, "RELATION EXTRACTION", "NLP PIPELINE", "Elnagar et al. (2022)"),
        (43, "CONCEPT EXTRACTION", "NLP PIPELINE", "Taye et al. (2023)"),
        (44, "RELATION EXTRACTION", "TRANSFORMER-BASED", "Taye et al. (2023)"),
        (45, "CONCEPT EXTRACTION", "LSTM", "Al-Aswadi et al. (2023)"),
        (46, "ONTOLOGY ALIGNMENT", "ZERO-SHOT LLM", "He et al. (2023)"),
        (47, "CONCEPT EXTRACTION", "ZERO-SHOT LLM", "Babaei et al. (2023)"),
        (48, "TAXONOMY EXTRACTION", "FINE-TUNED LLM", "Babaei et al. (2023)"),
        (49, "RELATION EXTRACTION", "FINE-TUNED LLM", "Babaei et al. (2023)"),
        (50, "TEXT-TO-ONTOLOGY", "SPECIFIC", "Schaeffer et al. (2023)"),
        (51, "ONTOLOGY MATCHING", "FEW-SHOT LLM", "Hertling et al. (2023)"),
        (52, "ONTOLOGY MAPPING", "LSTM", "Zhao et al. (2023)"),
        (53, "ONTOLOGY MAPPING", "CNN", "Zhao et al. (2023)"),
        (54, "ONTOLOGY MAPPING", "ENCODER/DECODER", "Zhao et al. (2023)"),
        (55, "TEXT-TO-ONTOLOGY", "ZERO-SHOT LLM", "Mateiu et al. (2023)"),
        (56, "RELATION EXTRACTION", "TRANSFORMER-BASED", "Hari et al. (2023)")
    ]
    data_2 = [
        (57, "DOMAIN ONTOLOGY", "TRANSFORMER-BASED", "Yin et al. (2024)"),
        (58, "CONCEPT EXTRACTION", "ZERO-SHOT LLM", "Dong et al. (2024)"),
        (59, "CONCEPT EXTRACTION", "FINE-TUNED LLM", "Dong et al. (2024)"),
        (60, "RELATION EXTRACTION", "ZERO-SHOT LLM", "Dong et al. (2024)"),
        (61, "RELATION EXTRACTION", "FINE-TUNED LLM", "Dong et al. (2024)"),
        (62, "DOMAIN ONTOLOGY", "ZERO-SHOT LLM", "Yang et al. (2024)"),
        (63, "INSTANTIATION", "TRANSFORMER-BASED", "Al-Subhi et al. (2024)"),
        (64, "RELATION EXTRACTION", "SKIP-GRAM", "Basheer et al. (2024)"),
        (65, "CONCEPT EXTRACTION", "FEW-SHOT LLM", "Mai et al. (2024)"),
        (66, "TAXONOMY EXTRACTION", "FEW-SHOT LLM", "Mai et al. (2024)"),
        (67, "RELATION EXTRACTION", "FEW-SHOT LLM", "Mai et al. (2024)"),
        (68, "CONCEPT DISCOVERY", "RAG", "Toro et al. (2024)"),
        (69, "CONCEPT DISCOVERY", "ZERO-SHOT LLM", "Toro et al. (2024)"),
        (70, "RELATION EXTRACTION", "RAG", "Toro et al. (2024)"),
        (71, "RELATION EXTRACTION", "ZERO-SHOT LLM", "Toro et al. (2024)"),
        (72, "FRAMEWORK", "FINE-TUNED LLM", "Lo et al. (2024)"),
        (73, "RELATION EXTRACTION", "TRANSFORMER-BASED", "Pisu et al. (2024)"),
        (74, "TEXT-TO-ONTOLOGY", "ZERO-SHOT LLM", "Abolhasani et al. (2024)"),
        (75, "FRAMEWORK", "FEW-SHOT LLM", "Coutinho et al. (2024)"),
        (76, "ANNOTATIONS GENERATION", "ZERO-SHOT LLM", "Bischof et al. (2024)"),
        (77, "DOMAIN ONTOLOGY", "ZERO-SHOT LLM", "Fathallah et al. (2024, a)"),
        (78, "FRAMEWORK", "ZERO-SHOT LLM", "Fathallah et al. (2024, b)"),
        (79, "DOMAIN ONTOLOGY", "ZERO-SHOT LLM", "Dasilva et al. (2024)"),
        (80, "DOMAIN ONTOLOGY", "FEW-SHOT LLM", "Dasilva et al. (2024)"),
        (81, "COMPETENCY QUESTIONS GENERATION", "ZERO-SHOT LLM", "Zhang et al. (2024)"),
        (82, "DOMAIN ONTOLOGY", "EMBEDDING", "Huang et al. (2024)"),
        (83, "TEXT-TO-ONTOLOGY", "ZERO-SHOT LLM", "Bakker et al. (2024)"),
        (84, "COMPETENCY QUESTIONS GENERATION", "ZERO-SHOT LLM", "Feng et al. (2024)"),
        (85, "RELATION EXTRACTION", "ZERO-SHOT LLM", "Feng et al. (2024)"),
        (86, "ONTOLOGY MATCHING", "ZERO-SHOT LLM", "Feng et al. (2024)"),
        (87, "CONCEPT EXTRACTION", "RAG", "Sanaei et al. (2024)"),
        (88, "TAXONOMY EXTRACTION", "RAG", "Sanaei et al. (2024)"),
        (89, "RELATION EXTRACTION", "RAG", "Sanaei et al. (2024)"),
        (90, "CONCEPT LEARNING", "ZERO-SHOT LLM", "Goyal et al. (2024)"),
        (91, "CONCEPT LEARNING", "FEW-SHOT LLM", "Goyal et al. (2024)"),
        (92, "TAXONOMY EXTRACTION", "FEW-SHOT LLM", "Goyal et al. (2024)"),
        (93, "RELATION EXTRACTION", "FEW-SHOT LLM", "Goyal et al. (2024)"),
        (94, "DOMAIN ONTOLOGY", "ZERO-SHOT LLM", "Joachimiak et al. (2024)"),
        (95, "CONCEPT EXTRACTION", "FINE-TUNED LLM", "Ymele et al. (2024)"),
        (96, "TAXONOMY EXTRACTION", "FINE-TUNED LLM", "Ymele et al. (2024)"),
        (97, "RELATION EXTRACTION", "FINE-TUNED LLM", "Ymele et al. (2024)"),
        (98, "FRAMEWORK", "FEW-SHOT LLM", "Lippolis et al. (2025)"),
        (99, "TEXT-TO-ONTOLOGY", "FEW-SHOT LLM", "Bosso et al. (2025)")
    ]

    tasks = ["RELATION EXTRACTION", "CONCEPT EXTRACTION", "TAXONOMY EXTRACTION", "ONTOLOGY MATCHING", "CONCEPT LEARNING", "ONTOLOGY MAPPING", "AXIOM LEARNING", "RULE LEARNING", "TERMS CLUSTERING", "ONTOLOGY ALIGNMENT", "TEXT-TO-ONTOLOGY", "DOMAIN ONTOLOGY", "INSTANTIATION", "CONCEPT DISCOVERY", "FRAMEWORK", "ANNOTATIONS GENERATION", " COMPETENCY QUESTIONS GENERATION"]
    tasks_1 = ["RELATION EXTRACTION", "CONCEPT EXTRACTION", "CONCEPT LEARNING", "TAXONOMY EXTRACTION", "RULE LEARNING", "ONTOLOGY MATCHING", "ONTOLOGY MAPPING", "AXIOM LEARNING", "TERMS CLUSTERING", "ONTOLOGY ALIGNMENT", "TEXT-TO-ONTOLOGY"]
    tasks_2 = ["RELATION EXTRACTION", "CONCEPT EXTRACTION", "TAXONOMY EXTRACTION", "ONTOLOGY MATCHING", "CONCEPT LEARNING", "TEXT-TO-ONTOLOGY", "DOMAIN ONTOLOGY", "INSTANTIATION", "CONCEPT DISCOVERY", "FRAMEWORK", "ANNOTATIONS GENERATION", "COMPETENCY QUESTIONS GENERATION"]


    strategies = ["DISTRIBUTIONAL SEMANTICS", "SPECIFIC", "CBOW", "SKIP-GRAM", "NLP PIPELINE", "PATTERN MINING", "REGUALAR EXPRESSIONS", "RNN", "ENCODER/DECODER", "RULE-BASED", "EMBEDDING", "CNN", "LSTM", "LATENT DIRICHLET ANALYSIS", "ATTENTION-BASED", "EVOLUTIONARY ALGORITHM", "TRANSFORMER-BASED", "ZERO-SHOT LLM", "FINE-TUNED LLM", "FEW-SHOT LLM", "RAG"]    
    strategies_1 = ["DISTRIBUTIONAL SEMANTICS", "SPECIFIC", "CBOW", "SKIP-GRAM", "NLP PIPELINE", "PATTERN MINING", "REGULAR EXPRESSIONS", "RNN", "ENCODER/DECODER", "RULE-BASED", "EMBEDDING", "CNN", "LSTM", "LATENT DIRICHLET ANALYSIS", "ATTENTION-BASED", "EVOLUTIONARY ALGORITHM", "TRANSFORMER-BASED", "ZERO-SHOT LLM", "FINE-TUNED LLM", "FEW-SHOT LLM"]    
    strategies_2 = ["SKIP-GRAM", "EMBEDDING", "TRANSFORMER-BASED", "ZERO-SHOT LLM", "FINE-TUNED LLM", "FEW-SHOT LLM", "RAG"]    


    task_to_x = {task: i for i, task in enumerate(tasks_2)}
    strategy_to_y = {strategy: i for i, strategy in enumerate(strategies_2)}

    base_fontsize = 16      
    label_fontsize = 16

    fig, ax = plt.subplots(figsize=(17, 13))

    texts = []
    positions = []  
    offset_value = 0  # small vertical offset for all labels

    for _, task, strategy, author in data_2:
        x = task_to_x[task]
        y = strategy_to_y[strategy]

        # Scatter point
        ax.scatter(x, y, s=200, edgecolor='black', facecolor='skyblue', zorder=5)

        # Add label slightly above
        label = ax.text(x, y + offset_value, author, ha='center', va='center', fontsize=13, zorder=5)
        texts.append(label)
        positions.append((x, y))

    # Adjust text and draw arrows for all labels
    adjust_text(
        texts,
        ax=ax,
        arrowprops=dict(arrowstyle="->", color='gray', lw=0.7),
        expand_points=(1.2, 1.2),
        expand_text=(1.2, 1.2),
    )

    for (x, y), label in zip(positions, texts):
        lx, ly = label.get_position()
        ax.plot([x, lx], [y, ly], color='gray', lw=0.5, zorder=3)

    # Axis setup
    ax.set_xticks(range(len(tasks_2)))
    ax.set_xticklabels(tasks_2, fontsize=base_fontsize)
    ax.set_yticks(range(len(strategies_2)))
    ax.set_yticklabels(strategies_2, fontsize=base_fontsize)
    ax.set_xlabel("Tasks", fontsize=base_fontsize + 2, fontweight='bold')
    ax.set_ylabel("Strategies", fontsize=base_fontsize + 2, fontweight='bold')
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    ax.grid(True, linestyle='--', alpha=0.4)
    plt.rcParams.update({'font.size': base_fontsize})
    plt.tight_layout()
    plt.show()

def create_pie_chart(labels, values):
    # Create pie chart
    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct='%1.2f%%', startangle=140)

    # Title
    plt.title('Distribution of Types for Manual Ontology Methodologies')

    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')

    # Show chart
    plt.show()

def create_sankey_chart():
    #labels = ['Project', 'Framework', 'Integration', 'Linguistic', 'Expertise', 'Generality', 'Documents', 'Agility', 'Rigorousness', 'Evaluation', 'Top-Down', 'Middle-Out', 'Bottom-Up']
    labels_1 = ['Wang et al.', 'Rani et al.', 'Qiu et al.', 'Fawei et al.', 'Chandolikar et al.', 'Dera et al.', 'Ma et al.', 'Zhao et al.', 'ten Haaf et al.', 'ElAssy et al.', 'Tang et al.', 'Mesmia et al.', 'Pan et al.', 'Sobhogol et al.', 'Kommineni et al.', 'Doumanas et al.', 'Huang et al.', 'Wu et al.', 'Gadusu et al.', 'Lichtnow et al.'] 
    labels_2 = ['Creation and/or experts\' revision', 'Middle-out', 'Scraping', 'Relational database', 'Ontology Development 101', 'NeOn', 'HCOME', 'UponLite', 'McGinty et al.']
    labels_3 = ['Spanning Tree', 'Singular Value Decomposition', 'Semantic Similarity', 'Stanford CoreNLP', 'LSTM','Model Checking', 'Clustering', 'Specific procedure', 'LLM-based', 'Association Rules']
    

    # Step 2: Create Sankey diagram with intermediate layers
    fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = labels_1 + labels_2 + labels_3,
      color = "blue"
    ),
    link = dict(
      source = [20, 20, 21, 20, 22, 22, 23, 22, 22, 20, 24, 22, 25, 23, 20, 26, 27, 20, 28, 24,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 
      target = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 29, 30, 31, 32, 33, 32, 34, 31, 35, 36, 37, 36, 36, 36, 37, 37, 37, 38, 36, 37],
      value  = [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1]
    ))])

    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    fig.show()


    """ 
    source = [10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]  
    target = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9]
    value =  [9, 8, 5, 1, 1, 6, 5, 2, 2, 2, 4, 1, 12, 7, 9, 4, 12, 9, 11, 16, 6, 6, 13, 10, 12, 10, 10, 2, 9, 6, 4, 1, 4, 0, 2, 1]
    

    source = [0, 0, 3, 0, 6, 0, 0, 0, 0, 0, 0,  9, 11, 12, 13,  0,  0,  0,  0,  0,  9, 15, 16, 16]
    target = [1, 2, 4, 5, 7, 1, 8, 1, 7, 1, 7, 10, 10,  7, 10, 10, 10, 10, 10, 14, 10, 17,  8, 18]
    value =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """

    """ link_colors = (
        ['rgba(148, 103, 189, 0.6)'] * 4 +   # From Top-Down
        ['rgba(140, 86, 75, 0.6)']  * 4 +   # From Middle-Out
        ['rgba(227, 119, 194, 0.6)'] * 4 +   # From Bottom-Up
        ['rgba(31, 119, 180, 0.6)'] * 6 +   # From Project
        ['rgba(255, 127, 14, 0.6)'] * 6 +   # From Framework
        ['rgba(44, 160, 44, 0.6)'] * 6 +    # From Integration
        ['rgba(214, 39, 40, 0.6)'] * 6      # From Linguistic
    ) 

    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.7),
            label=labels
        ),
        link=dict(
            source=source,
            target=target,
            value=value
            #color=link_colors
        )
    )]) 

    fig.update_layout(title_text="Sankey Diagram with Source-Colored Links", font_size=20)
    fig.show() """

if __name__ == "__main__":
    labels = ['Project', 'Framework', 'Integration', 'Linguistic']
    values = [26.09, 34.78, 30.43, 8.70]

    #create_pie_chart(labels, values)
    #create_sankey_chart()
    create_chart_automatic()