var labels = ["Naive Bayes", "Logistic Regression", "Decision Tree","Random Forest"];
var accuracies = [94.04, 98.86, 99.6, 98.61];

var trace = {
    x: labels,
    y: accuracies,
    type: "bar",
    text: accuracies.map(String),
    textposition: 'auto',
    hoverinfo: 'none',
    marker: {
        color: 'light blue',
        opacity: 0.8,
        line: {
            width: 1.5
        }
  }
};

var layout = {
    title: "Machine Learning Models on Predicting News Article Validity",
    xaxis: {title: "Model Types"},
    yaxis: {title: "Accuracy Score (%)",
            range: [90, 100],
            tickvals:[90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    }
};

Plotly.newPlot("plotArea", [trace], layout)