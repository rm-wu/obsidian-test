2024.10.13-1328
Status: 
Tags: [[SSL]] [[Deep Learning]] [[Computer Vision]] #paper #note


# Image World Models

This is a quick note on the paper about Image World Models titled "Learning and Leveraging World Models in Visual Representation Learning"

How? Use the idea of World Models, i.e., the model predicts the outcome of doing a certain action.  Data Augmentation ←→ "actions"

![[IMW_scheme.png]]

JEPA is based on latent in-painting, while IMW extends it to handle photometric transformations and uses the world model $p_\phi$ also in the inference step of the model.

**Joint Embedding (Middle):** the predictor $p_\phi(z)=z$   is the identity, then the embedding network will only learn to encode what is shared between the input $y$ and its transformation $x$ (Note: this is what is usually done in contrastive learning)

**Generative World Model // JEPA World Model:**  They have a more expressive predictor/decoder which can be used to "undo" the transformation (or apply the transformation we are trying to predict)

Equivariant Representation Learning: the predictor $p_\phi(\cdot)$ can effectively 

Note on equivariance and 
**Equivariance**
A function $f$ is said to be equivariant wrt a group of transformations if applying a transformation to the input ($T(\cdot)$) and then applying the function is the same as first applying the function $f(\cdot)$ and then applying (a potentially different but related) transformation ($T'(\cdot)$) to the output:
$$
f(T(x)) = T'(f(x))
$$
**Invariance**
A function can be invariant wrt to a group of transformations if applying the transformation to the input does not change the output of the function. 
$$
f(T(x)) = f(x)
$$


---
### References
>[!example]- Paper
>![[2403.00504v1-2.pdf]]


