# ECE510
Github repo for ECE510 Course work.
This readme contains only the documenatation structure for the Main project. For Challenges and Codefests, Please check out github wiki page. https://github.com/TestBencher/ECE510/wiki
The main documentation for the project is within the Final Project folder and is named as Chiplet Design.docx


FPGA-Based Shape Classifier Accelerator (ECE 510 Final Project)

This project demonstrates a hardware-accelerated shape recognition system implemented on the Nexys 4 DDR FPGA board. The system detects simple geometric shapes (circle, square, triangle) using a logistic regression classifier trained offline in Python and synthesized into Verilog for real-time edge detection and classification.

---

## Project Goals

- Create an FPGA-based accelerator that classifies **circle, square, triangle**
- Replace multi-sensor input with a **single camera or simulated image input**
- Use edge detection + logistic regression to perform classification
- Demonstrate shape classification using LEDs and 7-segment display
- Benchmark **software vs hardware** in terms of accuracy and speed

---

## ML Model

- **Algorithm:** Multinomial Logistic Regression
- **Training:** Done in Python using `scikit-learn`
- **Input format:** Flattened 8×8 binary edge maps
- **Output:** Class label ∈ {0: Triangle, 1: Square, 2: Circle}
- **Accuracy:** 98.5% on test set of 1000 samples

---

## Hardware Design

- **Language:** Verilog (synthesizable RTL)
- **Target FPGA:** Nexys 4 DDR (Artix-7)
- **Modules:**
  - `sobel_edge_detector.v` – basic edge detection
  - `shape_classifier.v` – quantized logistic regression model
  - `top.v` – integrates classifier, LEDs, and 7-segment display

---

## Verification & Benchmarking

| Aspect              | Value                      |
|---------------------|----------------------------|
| Accuracy (Python)   | 98.5%                      |
| Accuracy (Hardware) | ~97% (across 1000 samples)|
| Speedup (HW vs SW)  | ~400× faster than Python   |
| Functional Match    | Verified on >100 samples |
| Automation          | .mem generator + testbench |

---

## Running the Project

### Software
1. Run `train_logistic.py` to train the model and export weights
2. Run `verilog_param_generator.py` to convert weights to Verilog `initial` blocks

### Hardware (Vivado)
1. Add RTL and `top.v` as design sources
2. Import weights via `shape_classifier.v` initial block
3. Generate bitstream and program FPGA
4. Watch output on 7-segment display and LEDs

---

## Acknowledgements

This project was made possible with technical support from **ChatGPT**, which assisted in:
- Design debugging
- Verilog generation
- Edge detection logic
- Python–Verilog integration
- Simulation automation and benchmarking

---
## Documenatation

Check out Chiplet Design.docx for full documenatation 

