import torch
import torch.nn as nn
import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        # Première couche de convolution (image RGB → 32 filtres 3x3)
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)  # max pooling 2x2

        # Deuxième couche de convolution (32 → 64)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)

        # Couche entièrement connectée : 64*8*8 → 512
        self.fc1 = nn.Linear(64 * 8 * 8, 512)

        # Dropout (anti-overfitting)
        self.dropout = nn.Dropout(p=0.5)

        # Couche de sortie : 512 → 10 (softmax appliqué plus tard)
        self.fc2 = nn.Linear(512, 10)

    def forward(self, x):
        # Bloc 1 : conv + ReLU + pool
        x = self.pool(F.relu(self.conv1(x)))  # -> 32x16x16

        # Bloc 2 : conv + ReLU + pool
        x = self.pool(F.relu(self.conv2(x)))  # -> 64x8x8

        # Flatten
        x = x.view(-1, 64 * 8 * 8)  # -> 4096

        # FC + ReLU + Dropout
        x = F.relu(self.fc1(x))
        x = self.dropout(x)

        # Couche de sortie
        x = self.fc2(x)  # Pas de softmax ici car CrossEntropyLoss l'applique automatiquement

        return x
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Définition des blocs du CNN avec leurs tailles
layers = [
    ("Input", "3x32x32"),
    ("Conv2d 3→32\n(3x3)", "32x32x32"),
    ("MaxPool 2x2", "32x16x16"),
    ("Conv2d 32→64\n(3x3)", "64x16x16"),
    ("MaxPool 2x2", "64x8x8"),
    ("Flatten", "4096"),
    ("FC → 512", "512"),
    ("Dropout", "512"),
    ("FC → 10", "10")
]

# Création du graphique
fig, ax = plt.subplots(figsize=(12, 3))
ax.axis('off')

x_offset = 0.5
for i, (name, shape) in enumerate(layers):
    box = patches.FancyBboxPatch((x_offset + i * 1.8, 0.5), 1.6, 1.5,
                                 boxstyle="round,pad=0.05", edgecolor='black', facecolor='lightblue')
    ax.add_patch(box)
    ax.text(x_offset + i * 1.8 + 0.8, 1.5, name, ha='center', va='bottom', fontsize=10, weight='bold')
    ax.text(x_offset + i * 1.8 + 0.8, 0.9, shape, ha='center', va='bottom', fontsize=9)

plt.xlim(0, len(layers) * 2.2)
plt.ylim(0, 3)
plt.tight_layout()
plt.show()
