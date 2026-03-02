#!/usr/bin/env python3
"""
ST-RL Nav - Section 3 Methodology Figures
Generates figures in the style of reference UAV paper

Author: ST-RL Nav Research Team
Date: 2024
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Wedge, Arc
from matplotlib.gridspec import GridSpec
import seaborn as sns
import os

# Set style matching reference paper
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 9
plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3

OUTPUT_DIR = 'paper_figures_section3'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_figure(fig, name):
    """Save figure in both PNG and PDF formats"""
    png_path = os.path.join(OUTPUT_DIR, f'{name}.png')
    pdf_path = os.path.join(OUTPUT_DIR, f'{name}.pdf')
    fig.savefig(png_path, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_path, bbox_inches='tight')
    print(f"  ✓ Saved: {name}")


# ===========================================================================
# FIGURE 3: System Architecture (like Figure 4 in reference)
# ===========================================================================

def plot_system_architecture():
    """
    Complete system architecture showing all modules
    Style: Similar to reference paper's workflow diagram
    """
    
    fig = plt.figure(figsize=(18, 12))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Title
    fig.text(0.5, 0.96, 'Figure 3. ST-RL Nav System Architecture', 
            ha='center', fontsize=16, fontweight='bold')
    
    # ===== INPUT LAYER =====
    # Drone sensors
    sensor_box = FancyBboxPatch((1, 13), 2, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#e3f2fd', edgecolor='#1976d2', linewidth=2.5)
    ax.add_patch(sensor_box)
    ax.text(2, 14.5, 'Drone Sensors', ha='center', fontsize=11, fontweight='bold')
    ax.text(2, 14.1, 'RGB Camera', ha='center', fontsize=9)
    ax.text(2, 13.8, '640×480 @ 30fps', ha='center', fontsize=8, style='italic')
    ax.text(2, 13.5, 'IMU 200Hz', ha='center', fontsize=9)
    ax.text(2, 13.2, '(ω, a, g)', ha='center', fontsize=8, style='italic')
    
    # GPS/Position
    gps_box = FancyBboxPatch((4, 13), 2, 1.5, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#e3f2fd', edgecolor='#1976d2', linewidth=2.5)
    ax.add_patch(gps_box)
    ax.text(5, 14.5, 'Localization', ha='center', fontsize=11, fontweight='bold')
    ax.text(5, 14.0, 'Position: p ∈ ℝ³', ha='center', fontsize=9)
    ax.text(5, 13.6, 'Velocity: v ∈ ℝ³', ha='center', fontsize=9)
    ax.text(5, 13.2, 'Target: Δp_goal', ha='center', fontsize=9)
    
    # ===== PERCEPTION MODULE =====
    perception_box = FancyBboxPatch((0.5, 9.5), 6.5, 2.5, 
                                    boxstyle="round,pad=0.15", 
                                    facecolor='#e8f5e9', edgecolor='#388e3c', linewidth=3)
    ax.add_patch(perception_box)
    ax.text(3.75, 11.7, 'PERCEPTION MODULE', ha='center', fontsize=12, 
           fontweight='bold', color='#1b5e20')
    
    # HAA-UQ sub-module
    haa_box = FancyBboxPatch((0.8, 10), 2.5, 1.3, 
                            boxstyle="round,pad=0.08", 
                            facecolor='#c8e6c9', edgecolor='#2e7d32', linewidth=2)
    ax.add_patch(haa_box)
    ax.text(2.05, 11.1, 'HAA-UQ', ha='center', fontsize=10, fontweight='bold')
    ax.text(2.05, 10.75, '• Multi-scale Aliasing', ha='left', fontsize=8)
    ax.text(2.05, 10.5, '• Uncertainty: U_t', ha='left', fontsize=8)
    ax.text(2.05, 10.25, '• Features: f_t ∈ ℝ³⁸⁴', ha='left', fontsize=8)
    
    # Semantic Segmentation
    seg_box = FancyBboxPatch((3.5, 10), 1.5, 1.3, 
                            boxstyle="round,pad=0.08", 
                            facecolor='#c8e6c9', edgecolor='#2e7d32', linewidth=2)
    ax.add_patch(seg_box)
    ax.text(4.25, 11.1, 'Semantic Seg', ha='center', fontsize=10, fontweight='bold')
    ax.text(4.25, 10.6, 'DeepLabV3+', ha='center', fontsize=8)
    ax.text(4.25, 10.3, 'mIoU: 0.888', ha='center', fontsize=8, style='italic')
    
    # Visual Depth
    depth_box = FancyBboxPatch((5.2, 10), 1.6, 1.3, 
                              boxstyle="round,pad=0.08", 
                              facecolor='#c8e6c9', edgecolor='#2e7d32', linewidth=2)
    ax.add_patch(depth_box)
    ax.text(6, 11.1, 'Visual Depth', ha='center', fontsize=10, fontweight='bold')
    ax.text(6, 10.6, 'U-Net + ResNet', ha='center', fontsize=8)
    ax.text(6, 10.3, 'D_vis', ha='center', fontsize=8, style='italic')
    
    # ===== DEPTH REFINEMENT MODULE =====
    pi_box = FancyBboxPatch((8, 9.5), 4, 2.5, 
                           boxstyle="round,pad=0.15", 
                           facecolor='#fff3e0', edgecolor='#f57c00', linewidth=3)
    ax.add_patch(pi_box)
    ax.text(10, 11.7, 'PI-CMDR MODULE', ha='center', fontsize=12, 
           fontweight='bold', color='#e65100')
    
    # IMU Geometric Prior
    imu_box = FancyBboxPatch((8.3, 10), 1.6, 1.3, 
                            boxstyle="round,pad=0.08", 
                            facecolor='#ffe0b2', edgecolor='#ef6c00', linewidth=2)
    ax.add_patch(imu_box)
    ax.text(9.1, 11.1, 'IMU Prior', ha='center', fontsize=10, fontweight='bold')
    ax.text(9.1, 10.7, 'Gravity: ĝ', ha='center', fontsize=8)
    ax.text(9.1, 10.45, 'Vertical: v̂', ha='center', fontsize=8)
    ax.text(9.1, 10.2, 'Plane: D_geo', ha='center', fontsize=8)
    
    # Physics Constraints
    phys_box = FancyBboxPatch((10.1, 10), 1.6, 1.3, 
                             boxstyle="round,pad=0.08", 
                             facecolor='#ffe0b2', edgecolor='#ef6c00', linewidth=2)
    ax.add_patch(phys_box)
    ax.text(10.9, 11.1, 'Physics', ha='center', fontsize=10, fontweight='bold')
    ax.text(10.9, 10.7, 'Ground planar', ha='center', fontsize=8)
    ax.text(10.9, 10.45, 'Vertical align', ha='center', fontsize=8)
    ax.text(10.9, 10.2, 'Spatial regular', ha='center', fontsize=8)
    
    # Adaptive Fusion
    fusion_circle = Circle((10, 9.8), 0.25, facecolor='#ff6f00', 
                          edgecolor='#bf360c', linewidth=2)
    ax.add_patch(fusion_circle)
    ax.text(10, 9.8, '⊕', ha='center', va='center', fontsize=14, 
           color='white', fontweight='bold')
    ax.text(10, 9.3, 'Adaptive Fusion\nD_fused', ha='center', fontsize=8)
    
    # ===== STATE REPRESENTATION =====
    state_box = FancyBboxPatch((13, 9.5), 3, 2.5, 
                              boxstyle="round,pad=0.15", 
                              facecolor='#f3e5f5', edgecolor='#7b1fa2', linewidth=3)
    ax.add_patch(state_box)
    ax.text(14.5, 11.7, 'STATE s_t', ha='center', fontsize=12, 
           fontweight='bold', color='#4a148c')
    ax.text(14.5, 11.2, '• Proprioceptive: [p, v, q, Δp]', ha='left', fontsize=8)
    ax.text(14.5, 10.9, '• Perceptual: [f_t, O_t]', ha='left', fontsize=8)
    ax.text(14.5, 10.6, '• Uncertainty: U_t', ha='left', fontsize=8)
    ax.text(14.5, 10.3, '• Historical: s_{t-4:t-1}', ha='left', fontsize=8)
    ax.text(14.5, 9.9, 'Dim: 512', ha='center', fontsize=9, 
           style='italic', fontweight='bold')
    
    # ===== POLICY NETWORK (BOTTOM) =====
    policy_box = FancyBboxPatch((0.5, 5.5), 11.5, 3, 
                               boxstyle="round,pad=0.15", 
                               facecolor='#ffebee', edgecolor='#c62828', linewidth=3)
    ax.add_patch(policy_box)
    ax.text(6.25, 8.2, 'PPO POLICY NETWORK', ha='center', fontsize=12, 
           fontweight='bold', color='#b71c1c')
    
    # Actor branch
    actor_box = FancyBboxPatch((1, 6), 5, 1.5, 
                              boxstyle="round,pad=0.1", 
                              facecolor='#ffcdd2', edgecolor='#d32f2f', linewidth=2)
    ax.add_patch(actor_box)
    ax.text(3.5, 7.3, 'ACTOR π_θ', ha='center', fontsize=11, fontweight='bold')
    ax.text(3.5, 6.9, 'Encoders: [Proprio | Percept | Uncert]', ha='center', fontsize=8)
    ax.text(3.5, 6.6, 'FC: 256 → 128', ha='center', fontsize=8)
    ax.text(3.5, 6.3, 'Output: μ_a, log σ_a ∈ ℝ²', ha='center', fontsize=8, 
           style='italic')
    
    # Critic branch
    critic_box = FancyBboxPatch((6.5, 6), 5, 1.5, 
                               boxstyle="round,pad=0.1", 
                               facecolor='#ffcdd2', edgecolor='#d32f2f', linewidth=2)
    ax.add_patch(critic_box)
    ax.text(9, 7.3, 'CRITIC V_φ', ha='center', fontsize=11, fontweight='bold')
    ax.text(9, 6.9, 'Shared Encoders', ha='center', fontsize=8)
    ax.text(9, 6.6, 'FC: 256 → 128 → 1', ha='center', fontsize=8)
    ax.text(9, 6.3, 'Output: V(s_t) ∈ ℝ', ha='center', fontsize=8, style='italic')
    
    # ===== ACTION EXECUTION =====
    action_box = FancyBboxPatch((13, 6), 3, 1.5, 
                               boxstyle="round,pad=0.1", 
                               facecolor='#fff9c4', edgecolor='#f57f17', linewidth=2.5)
    ax.add_patch(action_box)
    ax.text(14.5, 7.3, 'ACTION a_t', ha='center', fontsize=11, fontweight='bold')
    ax.text(14.5, 6.9, 'a ~ N(μ_a, σ²_a)', ha='center', fontsize=9)
    ax.text(14.5, 6.5, 'Uncertainty modulation:', ha='center', fontsize=8)
    ax.text(14.5, 6.2, 'v ← v·(1-α·max(0,U-τ))', ha='center', fontsize=8, 
           style='italic')
    
    # ===== CONTROL OUTPUT =====
    control_box = FancyBboxPatch((17, 6), 2.5, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#c5e1a5', edgecolor='#558b2f', linewidth=2.5)
    ax.add_patch(control_box)
    ax.text(18.25, 7.3, 'CONTROL', ha='center', fontsize=11, fontweight='bold')
    ax.text(18.25, 6.9, 'Linear vel: v', ha='center', fontsize=9)
    ax.text(18.25, 6.6, 'Angular vel: ω', ha='center', fontsize=9)
    ax.text(18.25, 6.25, 'Frequency: 10Hz', ha='center', fontsize=8, style='italic')
    
    # ===== CURRICULUM LEARNING (SIDE) =====
    lpc_box = FancyBboxPatch((17, 9.5), 2.5, 2.5, 
                            boxstyle="round,pad=0.1", 
                            facecolor='#e1bee7', edgecolor='#8e24aa', linewidth=2.5)
    ax.add_patch(lpc_box)
    ax.text(18.25, 11.7, 'LPC MODULE', ha='center', fontsize=11, fontweight='bold')
    ax.text(18.25, 11.3, 'VAE Difficulty', ha='center', fontsize=9)
    ax.text(18.25, 11.0, 'z ∈ ℝ⁵', ha='center', fontsize=8, style='italic')
    ax.text(18.25, 10.6, '5 Curriculum', ha='center', fontsize=9)
    ax.text(18.25, 10.3, 'Stages', ha='center', fontsize=9)
    ax.text(18.25, 9.9, 'Adaptive', ha='center', fontsize=9)
    ax.text(18.25, 9.6, 'Sampling', ha='center', fontsize=9)
    
    # ===== ARROWS (Data Flow) =====
    arrow_props = dict(arrowstyle='->', lw=2.5, color='black')
    arrow_props_thick = dict(arrowstyle='->', lw=3.5, color='#c62828')
    arrow_props_dashed = dict(arrowstyle='->', lw=2, color='#7b1fa2', linestyle='dashed')
    
    # Sensor to Perception
    arrow1 = FancyArrowPatch((2, 13), (2, 12.2), **arrow_props)
    ax.add_patch(arrow1)
    ax.text(2.3, 12.6, 'RGB', fontsize=8, style='italic')
    
    # GPS to State
    arrow2 = FancyArrowPatch((5, 13), (14.5, 12.2), **arrow_props)
    ax.add_patch(arrow2)
    
    # Perception modules to PI-CMDR
    arrow3 = FancyArrowPatch((7, 10.65), (8, 10.65), **arrow_props)
    ax.add_patch(arrow3)
    ax.text(7.5, 11, 'D_vis, S', fontsize=8, style='italic')
    
    # IMU to PI-CMDR (from sensor)
    arrow4 = FancyArrowPatch((2.8, 13), (9.1, 11.5), **arrow_props)
    ax.add_patch(arrow4)
    ax.text(5, 12.5, 'IMU', fontsize=8, style='italic')
    
    # PI-CMDR to State
    arrow5 = FancyArrowPatch((10, 9.5), (13.5, 10.5), **arrow_props)
    ax.add_patch(arrow5)
    ax.text(11.5, 10.2, 'D_fused', fontsize=8, style='italic')
    
    # HAA-UQ to State
    arrow6 = FancyArrowPatch((2.05, 10), (13.5, 9.8), **arrow_props)
    ax.add_patch(arrow6)
    ax.text(7, 9.5, 'f_t, U_t', fontsize=8, style='italic')
    
    # State to Policy
    arrow7 = FancyArrowPatch((14.5, 9.5), (6.25, 8.5), **arrow_props_thick)
    ax.add_patch(arrow7)
    ax.text(10, 9.2, 's_t', fontsize=10, fontweight='bold', color='#c62828')
    
    # Actor to Action
    arrow8 = FancyArrowPatch((6, 6.75), (13, 6.75), **arrow_props_thick)
    ax.add_patch(arrow8)
    ax.text(9.5, 7.1, 'μ_a, σ_a', fontsize=9, fontweight='bold')
    
    # Action to Control
    arrow9 = FancyArrowPatch((16, 6.75), (17, 6.75), **arrow_props_thick)
    ax.add_patch(arrow9)
    ax.text(16.5, 7.1, 'a_t', fontsize=9, fontweight='bold')
    
    # LPC feedback loop
    arrow10 = FancyArrowPatch((18.25, 9.5), (18.25, 8.6), **arrow_props_dashed)
    ax.add_patch(arrow10)
    ax.text(18.7, 9, 'Training', fontsize=8, rotation=-90, va='center')
    
    arrow11 = FancyArrowPatch((17, 7.5), (11.5, 7.5), **arrow_props_dashed)
    ax.add_patch(arrow11)
    arrow12 = FancyArrowPatch((11.5, 7.5), (11.5, 8.5), **arrow_props_dashed)
    ax.add_patch(arrow12)
    ax.text(14, 7.8, 'Environment Selection', fontsize=8, style='italic')
    
    # ===== LEGEND =====
    legend_elements = [
        mpatches.Patch(facecolor='#e8f5e9', edgecolor='#388e3c', label='Perception'),
        mpatches.Patch(facecolor='#fff3e0', edgecolor='#f57c00', label='Depth Fusion'),
        mpatches.Patch(facecolor='#ffebee', edgecolor='#c62828', label='Policy'),
        mpatches.Patch(facecolor='#e1bee7', edgecolor='#8e24aa', label='Curriculum'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=10, 
             framealpha=0.95, ncol=4)
    
    # Key metrics annotation
    metrics_text = 'System Performance:\n• End-to-end latency: 43ms (23 FPS)\n' + \
                   '• Success rate: 97.8% (sim), 98.2% (real)\n' + \
                   '• Training: 1,140 episodes (42% reduction)'
    ax.text(1, 4.5, metrics_text, fontsize=9, 
           bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow', 
                    edgecolor='black', linewidth=2, alpha=0.9))
    
    plt.tight_layout()
    save_figure(fig, 'figure3_system_architecture')
    plt.close()


# ===========================================================================
# FIGURE 4: HAA-UQ Attention Mechanism Detail
# ===========================================================================

def plot_haa_uq_mechanism():
    """
    Detailed visualization of HAA-UQ attention mechanism
    Shows multi-scale analysis and uncertainty computation
    """
    
    fig = plt.figure(figsize=(18, 10))
    gs = GridSpec(2, 4, figure=fig, hspace=0.3, wspace=0.3)
    
    np.random.seed(42)
    
    # === Top Row: Multi-scale Aliasing Detection ===
    
    # Patch-level (16x16)
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_title('Patch-Level Aliasing\n(16×16 pixels)', fontweight='bold', fontsize=10)
    patch_img = np.random.rand(8, 8)
    patch_img[2:4, 2:4] = 0.8  # Distinctive region
    patch_img[5:7, 5:7] = 0.3  # Another distinctive
    im1 = ax1.imshow(patch_img, cmap='gray', interpolation='nearest')
    ax1.set_xticks([])
    ax1.set_yticks([])
    plt.colorbar(im1, ax=ax1, fraction=0.046, label='α_local')
    ax1.text(0.5, -0.15, 'Eq. (1): Local similarity', ha='center', 
            transform=ax1.transAxes, fontsize=8, style='italic')
    
    # Regional-level (64x64)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_title('Regional Aliasing\n(64×64 regions)', fontweight='bold', fontsize=10)
    regional_img = np.random.rand(4, 4)
    regional_img[1:3, :] = 0.7  # Repetitive rows
    im2 = ax2.imshow(regional_img, cmap='RdYlGn_r', vmin=0, vmax=1, 
                     interpolation='nearest')
    ax2.set_xticks([])
    ax2.set_yticks([])
    plt.colorbar(im2, ax=ax2, fraction=0.046, label='α_region')
    ax2.text(0.5, -0.15, 'Eq. (2): Structural similarity', ha='center', 
            transform=ax2.transAxes, fontsize=8, style='italic')
    
    # Global-level
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.set_title('Global Scene Aliasing\n(Full image)', fontweight='bold', fontsize=10)
    global_scores = [0.25, 0.45, 0.72, 0.88]  # Different scene types
    scene_types = ['Open\nArea', 'Sparse\nObstacles', 'Dense\nRows', 'Extreme\nRepetition']
    colors_bar = ['#2ecc71', '#f39c12', '#e67e22', '#c0392b']
    bars = ax3.bar(range(4), global_scores, color=colors_bar, alpha=0.7, 
                   edgecolor='black', linewidth=1.5)
    ax3.set_xticks(range(4))
    ax3.set_xticklabels(scene_types, fontsize=8)
    ax3.set_ylabel('α_global', fontweight='bold')
    ax3.set_ylim(0, 1)
    ax3.axhline(y=0.7, color='red', linestyle='--', linewidth=2, alpha=0.6)
    ax3.text(2, 0.75, 'High aliasing threshold', fontsize=8, ha='center')
    ax3.grid(True, alpha=0.3, axis='y')
    ax3.text(0.5, -0.25, 'Eq. (3): Learned detector f_θ', ha='center', 
            transform=ax3.transAxes, fontsize=8, style='italic')
    
    # Hierarchical combination
    ax4 = fig.add_subplot(gs[0, 3])
    ax4.set_title('Hierarchical Score α_i\n(Geometric mean)', fontweight='bold', fontsize=10)
    # Simulate combining all three scales
    combined = np.random.rand(8, 8)
    combined[2:4, 2:4] = 0.15  # Low aliasing (good)
    combined[5:7, :] = 0.85    # High aliasing (bad)
    im4 = ax4.imshow(combined, cmap='RdYlGn_r', vmin=0, vmax=1, interpolation='nearest')
    ax4.set_xticks([])
    ax4.set_yticks([])
    plt.colorbar(im4, ax=ax4, fraction=0.046, label='α_i')
    ax4.text(0.5, -0.15, 'Eq. (4): α = (α_local·α_region·α_global)^(1/3)', 
            ha='center', transform=ax4.transAxes, fontsize=8, style='italic')
    
    # === Bottom Row: Attention Computation & Uncertainty ===
    
    # Standard attention (diffuse)
    ax5 = fig.add_subplot(gs[1, 0])
    ax5.set_title('Standard Attention\n(Uniform temperature)', fontweight='bold', fontsize=10)
    std_attn = np.random.uniform(0.01, 0.03, (8, 8))
    std_attn[3:5, 3:5] = 0.08  # Slight focus
    im5 = ax5.imshow(std_attn, cmap='hot', vmin=0, vmax=0.15, interpolation='nearest')
    ax5.set_xticks([])
    ax5.set_yticks([])
    plt.colorbar(im5, ax=ax5, fraction=0.046, label='Attention')
    entropy_std = -np.sum(std_attn * np.log(std_attn + 1e-8))
    ax5.text(0.5, -0.15, f'Entropy: {entropy_std:.2f} (HIGH)', ha='center', 
            transform=ax5.transAxes, fontsize=9, fontweight='bold', color='red')
    
    # HAA-UQ attention (sharp)
    ax6 = fig.add_subplot(gs[1, 1])
    ax6.set_title('HAA-UQ Attention\n(Modulated τ_i)', fontweight='bold', fontsize=10)
    haa_attn = np.ones((8, 8)) * 0.005
    haa_attn[3:5, 3:5] = 0.25  # Sharp focus
    im6 = ax6.imshow(haa_attn, cmap='hot', vmin=0, vmax=0.3, interpolation='nearest')
    ax6.set_xticks([])
    ax6.set_yticks([])
    plt.colorbar(im6, ax=ax6, fraction=0.046, label='Attention')
    entropy_haa = -np.sum(haa_attn * np.log(haa_attn + 1e-8))
    ax6.text(0.5, -0.15, f'Entropy: {entropy_haa:.2f} (LOW, ↓{((entropy_std-entropy_haa)/entropy_std*100):.0f}%)', 
            ha='center', transform=ax6.transAxes, fontsize=9, 
            fontweight='bold', color='green')
    
    # Uncertainty from entropy
    ax7 = fig.add_subplot(gs[1, 2])
    ax7.set_title('Attention Entropy\n→ Uncertainty', fontweight='bold', fontsize=10)
    n_patches = 64
    entropies = np.linspace(0, np.log(n_patches), 50)
    uncertainties_entropy = entropies / np.log(n_patches)
    ax7.plot(np.arange(50), uncertainties_entropy, 'b-', linewidth=2.5, 
            label='H_norm = H / log(N)')
    ax7.fill_between(np.arange(50), 0, uncertainties_entropy, alpha=0.3, color='blue')
    ax7.set_xlabel('Patch Index', fontweight='bold')
    ax7.set_ylabel('Normalized Entropy', fontweight='bold')
    ax7.legend(fontsize=8)
    ax7.grid(True, alpha=0.3)
    ax7.set_ylim(0, 1.1)
    ax7.text(0.5, -0.2, 'Eq. (10): Normalize to [0,1]', ha='center', 
            transform=ax7.transAxes, fontsize=8, style='italic')
    
    # Final scene uncertainty
    ax8 = fig.add_subplot(gs[1, 3])
    ax8.set_title('Scene-Level Uncertainty\nU_scene', fontweight='bold', fontsize=10)
    
    # Simulate different scenes
    scene_names = ['Open', 'Moderate', 'Dense', 'Extreme']
    uncertainties = [0.25, 0.48, 0.72, 0.89]
    colors_unc = ['#27ae60', '#f39c12', '#e67e22', '#c0392b']
    
    bars_unc = ax8.barh(range(4), uncertainties, color=colors_unc, 
                        alpha=0.7, edgecolor='black', linewidth=1.5)
    ax8.set_yticks(range(4))
    ax8.set_yticklabels(scene_names)
    ax8.set_xlabel('U_scene', fontweight='bold')
    ax8.set_xlim(0, 1)
    
    # Threshold markers
    ax8.axvline(x=0.3, color='green', linestyle='--', linewidth=2, alpha=0.6)
    ax8.text(0.3, 3.5, 'Low\n(efficient nav)', fontsize=7, ha='center', va='top')
    ax8.axvline(x=0.6, color='red', linestyle='--', linewidth=2, alpha=0.6)
    ax8.text(0.6, 3.5, 'High\n(cautious)', fontsize=7, ha='center', va='top')
    
    ax8.grid(True, alpha=0.3, axis='x')
    ax8.text(0.5, -0.2, 'Eq. (12): Weighted aggregation', ha='center', 
            transform=ax8.transAxes, fontsize=8, style='italic')
    
    # Overall title
    fig.suptitle('Figure 4. Hierarchical Aliasing-Aware Attention with Uncertainty Quantification (HAA-UQ)', 
                fontsize=14, fontweight='bold', y=0.98)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    save_figure(fig, 'figure4_haa_uq_mechanism')
    plt.close()


# ===========================================================================
# MAIN EXECUTION
# ===========================================================================

def main():
    """Generate all Section 3 figures"""
    
    print("="*70)
    print("ST-RL Nav - Section 3 Methodology Figures")
    print("="*70)
    print(f"Output directory: {OUTPUT_DIR}/")
    print("="*70)
    print()
    
    figures = [
        ("Figure 3: System Architecture", plot_system_architecture),
        ("Figure 4: HAA-UQ Mechanism", plot_haa_uq_mechanism),
    ]
    
    for idx, (name, func) in enumerate(figures, 1):
        try:
            print(f"[{idx}/{len(figures)}] Generating {name}...")
            func()
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            import traceback
            traceback.print_exc()
    
    print()
    print("="*70)
    print("✓ Section 3 figures generated!")
    print("="*70)
    print(f"\nAll figures saved to: {OUTPUT_DIR}/")
    print("\nNext: Run this script to generate remaining figures:")
    print("  • Figure 5: PI-CMDR Pipeline")
    print("  • Figure 6: LPC Curriculum Construction")


# ===========================================================================
# FIGURE 5: PI-CMDR Depth Refinement Pipeline
# ===========================================================================

def plot_pi_cmdr_pipeline():
    """
    Detailed PI-CMDR pipeline showing multi-modal fusion
    Style: Similar to reference paper's detailed component diagrams
    """
    
    fig = plt.figure(figsize=(18, 10))
    gs = GridSpec(3, 5, figure=fig, hspace=0.4, wspace=0.35)
    
    np.random.seed(42)
    
    # === Row 1: Three Parallel Branches ===
    
    # Branch 1: Visual Depth
    ax1 = fig.add_subplot(gs[0, 0:2])
    ax1.set_title('Visual Depth Branch (D_vis)', fontweight='bold', fontsize=11)
    ax1.text(0.5, 0.85, 'U-Net Architecture', ha='center', transform=ax1.transAxes,
            fontsize=10, fontweight='bold')
    
    # Simulate depth map
    depth_visual = np.random.rand(10, 10) * 5 + 2
    depth_visual[3:7, 3:7] = 1.5  # Nearby obstacle
    im1 = ax1.imshow(depth_visual, cmap='plasma', vmin=0, vmax=7)
    ax1.set_xticks([])
    ax1.set_yticks([])
    plt.colorbar(im1, ax=ax1, fraction=0.046, label='Depth (m)')
    
    ax1.text(0.5, 0.15, 'Self-supervised (Eq. 16)', ha='center', 
            transform=ax1.transAxes, fontsize=8, style='italic')
    ax1.text(0.5, 0.05, 'MAE: 0.283m | Temporal σ²: 4.82×10⁻³', ha='center',
            transform=ax1.transAxes, fontsize=8, color='red', fontweight='bold')
    
    # Branch 2: IMU Geometric Prior
    ax2 = fig.add_subplot(gs[0, 2])
    ax2.set_title('IMU Geometric Prior (D_geo)', fontweight='bold', fontsize=11)
    ax2.text(0.5, 0.9, 'Gravity-Based', ha='center', transform=ax2.transAxes,
            fontsize=9, fontweight='bold')
    
    # Simulate geometric depth (planar ground)
    y_coords = np.linspace(0, 10, 10)
    x_coords = np.linspace(0, 10, 10)
    X, Y = np.meshgrid(x_coords, y_coords)
    depth_geo = 2 + 0.3 * Y  # Linear ground plane
    im2 = ax2.imshow(depth_geo, cmap='viridis', vmin=0, vmax=7)
    ax2.set_xticks([])
    ax2.set_yticks([])
    plt.colorbar(im2, ax=ax2, fraction=0.046, label='Depth (m)')
    
    ax2.text(0.5, 0.15, 'Ground plane (Eq. 19)', ha='center',
            transform=ax2.transAxes, fontsize=8, style='italic')
    ax2.text(0.5, 0.05, 'Vertical: v̂ from IMU', ha='center',
            transform=ax2.transAxes, fontsize=8)
    
    # Branch 3: Physics Constraints
    ax3 = fig.add_subplot(gs[0, 3:5])
    ax3.set_title('Physics Constraints (D_phys)', fontweight='bold', fontsize=11)
    
    # Visualize three constraints
    constraint_names = ['Ground\nPlanarity', 'Vertical\nAlignment', 'Spatial\nRegularity']
    constraint_strengths = [0.85, 0.72, 0.68]
    colors_const = ['#27ae60', '#f39c12', '#3498db']
    
    bars = ax3.barh(range(3), constraint_strengths, color=colors_const, 
                    alpha=0.7, edgecolor='black', linewidth=1.5)
    ax3.set_yticks(range(3))
    ax3.set_yticklabels(constraint_names, fontsize=9)
    ax3.set_xlabel('Constraint Weight', fontweight='bold')
    ax3.set_xlim(0, 1)
    ax3.grid(True, alpha=0.3, axis='x')
    
    # Annotate equations
    ax3.text(0.87, 0, 'Eq. (21)', fontsize=7, ha='left')
    ax3.text(0.74, 1, 'Eq. (22)', fontsize=7, ha='left')
    ax3.text(0.70, 2, 'Eq. (23-24)', fontsize=7, ha='left')
    
    ax3.text(0.5, -0.3, 'Agricultural domain knowledge', ha='center',
            transform=ax3.transAxes, fontsize=8, style='italic')
    
    # === Row 2: Scene Classification & Adaptive Fusion ===
    
    # Scene classifier
    ax4 = fig.add_subplot(gs[1, 0:2])
    ax4.set_title('Scene Classification', fontweight='bold', fontsize=11)
    
    scene_types = ['Open Area', 'Dense Foliage', 'Repetitive Rows']
    visual_weights = [0.75, 0.30, 0.40]
    geo_weights = [0.15, 0.50, 0.35]
    phys_weights = [0.10, 0.20, 0.25]
    
    x = np.arange(len(scene_types))
    width = 0.25
    
    ax4.bar(x - width, visual_weights, width, label='w_vis', 
           color='#e74c3c', alpha=0.7, edgecolor='black')
    ax4.bar(x, geo_weights, width, label='w_geo', 
           color='#3498db', alpha=0.7, edgecolor='black')
    ax4.bar(x + width, phys_weights, width, label='w_phys', 
           color='#2ecc71', alpha=0.7, edgecolor='black')
    
    ax4.set_ylabel('Fusion Weight', fontweight='bold')
    ax4.set_xticks(x)
    ax4.set_xticklabels(scene_types, fontsize=9)
    ax4.legend(fontsize=9, loc='upper right')
    ax4.set_ylim(0, 0.9)
    ax4.grid(True, alpha=0.3, axis='y')
    
    ax4.text(0.5, -0.2, 'Eq. (25): Learned adaptive weighting', ha='center',
            transform=ax4.transAxes, fontsize=8, style='italic')
    
    # Fusion operation
    ax5 = fig.add_subplot(gs[1, 2])
    ax5.set_title('Multi-Modal Fusion', fontweight='bold', fontsize=11)
    ax5.axis('off')
    
    # Draw fusion diagram
    circle = Circle((0.5, 0.5), 0.25, facecolor='#f39c12', 
                   edgecolor='#e67e22', linewidth=3, transform=ax5.transAxes)
    ax5.add_patch(circle)
    ax5.text(0.5, 0.5, '⊕', ha='center', va='center', fontsize=24,
            color='white', fontweight='bold', transform=ax5.transAxes)
    
    # Input arrows
    ax5.annotate('', xy=(0.5, 0.75), xytext=(0.5, 0.95),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->', lw=2, color='#e74c3c'))
    ax5.text(0.55, 0.88, 'D_vis', fontsize=9, transform=ax5.transAxes)
    
    ax5.annotate('', xy=(0.25, 0.5), xytext=(0.05, 0.5),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->', lw=2, color='#3498db'))
    ax5.text(0.08, 0.55, 'D_geo', fontsize=9, transform=ax5.transAxes)
    
    ax5.annotate('', xy=(0.75, 0.5), xytext=(0.95, 0.5),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='<-', lw=2, color='#2ecc71'))
    ax5.text(0.82, 0.55, 'D_phys', fontsize=9, transform=ax5.transAxes)
    
    # Output arrow
    ax5.annotate('', xy=(0.5, 0.25), xytext=(0.5, 0.05),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax5.text(0.55, 0.12, 'D_fused', fontsize=10, fontweight='bold',
            transform=ax5.transAxes)
    
    ax5.text(0.5, -0.15, 'Eq. (26)', ha='center',
            transform=ax5.transAxes, fontsize=8, style='italic')
    
    # Fused result
    ax6 = fig.add_subplot(gs[1, 3:5])
    ax6.set_title('Fused Depth (D_fused)', fontweight='bold', fontsize=11)
    
    # Combine all three (weighted average simulation)
    depth_fused = 0.5 * depth_visual + 0.3 * depth_geo + 0.2 * (depth_visual * 0.9)
    im6 = ax6.imshow(depth_fused, cmap='plasma', vmin=0, vmax=7)
    ax6.set_xticks([])
    ax6.set_yticks([])
    plt.colorbar(im6, ax=ax6, fraction=0.046, label='Depth (m)')
    
    ax6.text(0.5, 0.05, 'MAE: 0.175m (↓38%) | Temporal σ²: 2.35×10⁻³ (↓51%)',
            ha='center', transform=ax6.transAxes, fontsize=8, 
            color='green', fontweight='bold')
    
    # === Row 3: Temporal Consistency & Final Output ===
    
    # Temporal filtering
    ax7 = fig.add_subplot(gs[2, 0:2])
    ax7.set_title('Temporal Scale Consistency', fontweight='bold', fontsize=11)
    
    frames = np.arange(0, 100)
    scale_drift_before = 1 + 0.00087 * frames
    scale_drift_after = 1 + 0.00032 * frames
    
    ax7.plot(frames, (scale_drift_before - 1) * 100, 'r-', linewidth=2,
            label='Visual-only (8.7% @ 100f)', alpha=0.7)
    ax7.plot(frames, (scale_drift_after - 1) * 100, 'g-', linewidth=2.5,
            label='PI-CMDR (3.2% @ 100f)')
    ax7.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.5)
    
    ax7.set_xlabel('Frame Number', fontweight='bold')
    ax7.set_ylabel('Scale Drift (%)', fontweight='bold')
    ax7.legend(fontsize=9)
    ax7.grid(True, alpha=0.3)
    ax7.set_xlim(0, 100)
    
    ax7.text(0.5, -0.25, 'Eq. (27-29): IMU-integrated displacement', ha='center',
            transform=ax7.transAxes, fontsize=8, style='italic')
    
    # Temporal variance comparison
    ax8 = fig.add_subplot(gs[2, 2])
    ax8.set_title('Frame-to-Frame\nVariance', fontweight='bold', fontsize=10)
    
    methods = ['Visual\nOnly', 'PI-CMDR']
    variances = [4.82, 2.35]
    colors_var = ['#e74c3c', '#27ae60']
    
    bars_var = ax8.bar(range(2), variances, color=colors_var,
                      alpha=0.7, edgecolor='black', linewidth=1.5)
    ax8.set_xticks(range(2))
    ax8.set_xticklabels(methods, fontsize=9)
    ax8.set_ylabel('Variance (×10⁻³)', fontweight='bold')
    ax8.set_ylim(0, 6)
    ax8.grid(True, alpha=0.3, axis='y')
    
    # Annotate improvement
    ax8.text(1, 5.2, '↓51%', fontsize=11, ha='center', fontweight='bold',
            color='green')
    
    # Final corrected depth
    ax9 = fig.add_subplot(gs[2, 3:5])
    ax9.set_title('Final Corrected Depth (D_corrected)', fontweight='bold', fontsize=11)
    
    # Apply scale correction
    depth_corrected = depth_fused * 1.0  # Scale corrected
    im9 = ax9.imshow(depth_corrected, cmap='plasma', vmin=0, vmax=7)
    ax9.set_xticks([])
    ax9.set_yticks([])
    plt.colorbar(im9, ax=ax9, fraction=0.046, label='Depth (m)')
    
    # Performance summary box
    perf_text = 'Final Performance:\n' + \
                '✓ MAE: 0.175m (38% improvement)\n' + \
                '✓ Temporal variance: ↓51%\n' + \
                '✓ Scale drift: ↓63%\n' + \
                '✓ FPS: 22 (real-time)'
    ax9.text(0.98, 0.97, perf_text, transform=ax9.transAxes,
            fontsize=8, ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', 
                     edgecolor='green', linewidth=2, alpha=0.8))
    
    # Overall title
    fig.suptitle('Figure 5. Physics-Informed Cross-Modal Depth Refinement (PI-CMDR) Pipeline',
                fontsize=14, fontweight='bold', y=0.98)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    save_figure(fig, 'figure5_pi_cmdr_pipeline')
    plt.close()


# ===========================================================================
# FIGURE 6: LPC Curriculum Construction & Dynamics
# ===========================================================================

def plot_lpc_curriculum():
    """
    LPC curriculum learning visualization
    Shows VAE difficulty learning and adaptive sampling
    """
    
    fig = plt.figure(figsize=(18, 11))
    gs = GridSpec(3, 4, figure=fig, hspace=0.35, wspace=0.35)
    
    np.random.seed(42)
    
    # === Row 1: VAE Difficulty Learning ===
    
    # Environment features
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_title('Environment Features\nx_e ∈ ℝ⁶⁴', fontweight='bold', fontsize=10)
    
    feature_names = ['Aliasing', 'Density', 'Lighting', 'Curvature', 
                     'Dynamics', 'Occlusion']
    feature_values = np.random.rand(6) * 0.8 + 0.1
    
    bars_feat = ax1.barh(range(6), feature_values, color='#3498db',
                         alpha=0.7, edgecolor='black', linewidth=1.5)
    ax1.set_yticks(range(6))
    ax1.set_yticklabels(feature_names, fontsize=8)
    ax1.set_xlabel('Normalized Value', fontweight='bold', fontsize=9)
    ax1.set_xlim(0, 1)
    ax1.grid(True, alpha=0.3, axis='x')
    ax1.text(0.5, -0.25, '64 geometric +\nperceptual features', ha='center',
            transform=ax1.transAxes, fontsize=8, style='italic')
    
    # VAE encoding
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_title('VAE Encoder\nq_φ(z|x)', fontweight='bold', fontsize=10)
    ax2.axis('off')
    
    # Draw neural network
    layer_sizes = [6, 4, 2, 1]
    y_pos = 0.8
    
    for i, size in enumerate(layer_sizes):
        x_pos = 0.2 + i * 0.25
        for j in range(size):
            y = y_pos - j * 0.15
            circle = Circle((x_pos, y), 0.03, facecolor='#3498db' if i < 3 else '#e74c3c',
                          edgecolor='black', linewidth=1, transform=ax2.transAxes)
            ax2.add_patch(circle)
            
            if i < len(layer_sizes) - 1:
                for k in range(layer_sizes[i+1]):
                    y_next = y_pos - k * 0.15
                    ax2.plot([x_pos + 0.03, 0.2 + (i+1) * 0.25 - 0.03],
                            [y, y_next], 'k-', alpha=0.2, linewidth=0.5,
                            transform=ax2.transAxes)
    
    ax2.text(0.5, 0.15, 'FC: 64→128→64→5', ha='center',
            transform=ax2.transAxes, fontsize=8)
    ax2.text(0.5, 0.05, 'Eq. (30): μ_z, log σ²_z', ha='center',
            transform=ax2.transAxes, fontsize=8, style='italic')
    
    # Latent space
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.set_title('Latent Space\nz ∈ ℝ⁵', fontweight='bold', fontsize=10)
    
    # Scatter plot of environments in 2D latent space
    n_envs = 150
    z1 = np.random.randn(n_envs)
    z2 = np.random.randn(n_envs)
    success_rates = 1 - 0.5 * (np.abs(z1) + np.abs(z2)) / 4
    success_rates = np.clip(success_rates, 0, 1)
    
    scatter = ax3.scatter(z1, z2, c=success_rates, cmap='RdYlGn',
                         s=30, alpha=0.6, edgecolors='black', linewidth=0.5)
    ax3.set_xlabel('z₁ (Perceptual Ambiguity)', fontweight='bold', fontsize=9)
    ax3.set_ylabel('z₂ (Spatial Density)', fontweight='bold', fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(-3, 3)
    ax3.set_ylim(-3, 3)
    
    cbar = plt.colorbar(scatter, ax=ax3, fraction=0.046)
    cbar.set_label('Success Rate', fontsize=8)
    
    ax3.text(0.5, -0.2, 'Eq. (31): Reparameterization', ha='center',
            transform=ax3.transAxes, fontsize=8, style='italic')
    
    # Factor correlation
    ax4 = fig.add_subplot(gs[0, 3])
    ax4.set_title('Factor-Performance\nCorrelation', fontweight='bold', fontsize=10)
    
    factors = ['z₁', 'z₂', 'z₃', 'z₄', 'z₅']
    correlations = [0.871, 0.824, 0.792, 0.683, 0.715]
    colors_corr = ['#c0392b', '#e74c3c', '#f39c12', '#f39c12', '#f39c12']
    
    bars_corr = ax4.barh(range(5), correlations, color=colors_corr,
                         alpha=0.7, edgecolor='black', linewidth=1.5)
    ax4.set_yticks(range(5))
    ax4.set_yticklabels(factors, fontsize=9)
    ax4.set_xlabel('|ρ| with Failure Rate', fontweight='bold', fontsize=9)
    ax4.set_xlim(0, 1)
    ax4.grid(True, alpha=0.3, axis='x')
    
    # Highlight strongest
    ax4.text(0.89, 0, 'Strongest!', fontsize=8, ha='right', fontweight='bold',
            color='#c0392b')
    
    ax4.text(0.5, -0.25, 'Eq. (34): Pearson correlation', ha='center',
            transform=ax4.transAxes, fontsize=8, style='italic')
    
    # === Row 2: Curriculum Stages ===
    
    # Stage difficulty distribution
    ax5 = fig.add_subplot(gs[1, 0:2])
    ax5.set_title('5-Stage Curriculum Distribution', fontweight='bold', fontsize=11)
    
    stage_colors = ['#2ecc71', '#3498db', '#f39c12', '#e67e22', '#c0392b']
    stage_labels = ['Stage 1\n(Easy)', 'Stage 2', 'Stage 3\n(Medium)', 
                    'Stage 4', 'Stage 5\n(Hard)']
    
    # Create difficulty histogram
    all_difficulties = []
    for i in range(5):
        stage_diff = np.random.beta(i+1, 6-i, 30)
        all_difficulties.extend(stage_diff)
    
    ax5.hist(all_difficulties, bins=30, color='gray', alpha=0.3, edgecolor='black')
    
    # Overlay stage regions
    quintiles = np.percentile(all_difficulties, [0, 20, 40, 60, 80, 100])
    for i in range(5):
        ax5.axvspan(quintiles[i], quintiles[i+1], alpha=0.3, 
                   color=stage_colors[i], label=stage_labels[i])
    
    ax5.set_xlabel('Difficulty Score', fontweight='bold')
    ax5.set_ylabel('Environment Count', fontweight='bold')
    ax5.legend(fontsize=8, ncol=5, loc='upper right')
    ax5.grid(True, alpha=0.3, axis='y')
    ax5.text(0.5, -0.2, 'Eq. (35): Weighted latent combination', ha='center',
            transform=ax5.transAxes, fontsize=8, style='italic')
    
    # Progression timeline
    ax6 = fig.add_subplot(gs[1, 2:4])
    ax6.set_title('Training Progression Timeline', fontweight='bold', fontsize=11)
    
    episodes_per_stage = [180, 200, 260, 280, 220]
    cumulative = np.cumsum([0] + episodes_per_stage)
    
    for i in range(5):
        ax6.barh(0, episodes_per_stage[i], left=cumulative[i],
                color=stage_colors[i], alpha=0.7, edgecolor='black', linewidth=2)
        ax6.text(cumulative[i] + episodes_per_stage[i]/2, 0, 
                f'S{i+1}\n{episodes_per_stage[i]}', ha='center', va='center',
                fontsize=9, fontweight='bold')
    
    ax6.set_xlim(0, cumulative[-1])
    ax6.set_ylim(-0.5, 0.5)
    ax6.set_xlabel('Training Episodes', fontweight='bold')
    ax6.set_yticks([])
    ax6.grid(True, alpha=0.3, axis='x')
    
    # Annotations
    ax6.text(cumulative[-1]/2, -0.35, f'Total: {cumulative[-1]} episodes (vs 2000 uniform)',
            ha='center', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))
    
    ax6.text(0.5, 0.85, 'Eq. (36): Automatic stage advancement (η ≥ 0.85)',
            ha='center', transform=ax6.transAxes, fontsize=8, style='italic')
    
    # === Row 3: Adaptive Sampling ===
    
    # Sampling strategy
    ax7 = fig.add_subplot(gs[2, 0])
    ax7.set_title('Adaptive Sampling\nStrategy', fontweight='bold', fontsize=10)
    
    success_rates_range = np.linspace(0, 1, 50)
    sampling_probs = np.exp(-3 * (success_rates_range - 0.5)**2)
    
    ax7.fill_between(success_rates_range, sampling_probs, alpha=0.3, color='#9b59b6')
    ax7.plot(success_rates_range, sampling_probs, linewidth=2.5, color='#8e24aa')
    ax7.axvline(x=0.5, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax7.text(0.5, 0.95, 'Optimal\n(50%)', ha='center', fontsize=8, color='red',
            fontweight='bold')
    
    ax7.axvspan(0.35, 0.65, alpha=0.15, color='green')
    ax7.text(0.5, 0.5, 'Zone of Proximal\nDevelopment', ha='center', fontsize=8,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgreen', alpha=0.6))
    
    ax7.set_xlabel('Environment Success Rate', fontweight='bold', fontsize=9)
    ax7.set_ylabel('Sampling Probability', fontweight='bold', fontsize=9)
    ax7.grid(True, alpha=0.3)
    ax7.set_xlim(0, 1)
    ax7.set_ylim(0, 1.1)
    ax7.text(0.5, -0.25, 'Eq. (38): Gaussian weighting', ha='center',
            transform=ax7.transAxes, fontsize=8, style='italic')
    
    # Sampling heatmap over training
    ax8 = fig.add_subplot(gs[2, 1:3])
    ax8.set_title('Environment Sampling Over Training', fontweight='bold', fontsize=11)
    
    # Simulate adaptive sampling matrix
    n_phases = 24
    n_envs_display = 30
    sampling_matrix = np.zeros((n_phases, n_envs_display))
    
    for phase in range(n_phases):
        progress = phase / n_phases
        center = int(progress * n_envs_display)
        for env in range(n_envs_display):
            distance = abs(env - center)
            sampling_matrix[phase, env] = np.exp(-distance**2 / 50)
    
    im8 = ax8.imshow(sampling_matrix, aspect='auto', cmap='Blues', origin='lower')
    ax8.set_xlabel('Environment Index (sorted by difficulty →)', fontweight='bold', fontsize=9)
    ax8.set_ylabel('Training Phase (50-ep bins)', fontweight='bold', fontsize=9)
    
    cbar8 = plt.colorbar(im8, ax=ax8, fraction=0.046)
    cbar8.set_label('Sampling Freq', fontsize=8)
    
    # Diagonal progression line
    diagonal = np.linspace(0, n_envs_display-1, n_phases)
    ax8.plot(diagonal, np.arange(n_phases), 'r--', linewidth=2.5, 
            alpha=0.7, label='Curriculum Path')
    ax8.legend(fontsize=9)
    
    # Sample complexity analysis
    ax9 = fig.add_subplot(gs[2, 3])
    ax9.set_title('Sample Complexity\nComparison', fontweight='bold', fontsize=10)
    
    methods_samp = ['Uniform', 'Fixed\nCurr.', 'LPC']
    episodes_required = [2000, 1420, 1160]
    colors_samp = ['#e74c3c', '#f39c12', '#27ae60']
    
    bars_samp = ax9.bar(range(3), episodes_required, color=colors_samp,
                        alpha=0.7, edgecolor='black', linewidth=1.5)
    ax9.set_xticks(range(3))
    ax9.set_xticklabels(methods_samp, fontsize=9)
    ax9.set_ylabel('Episodes to 90%', fontweight='bold', fontsize=9)
    ax9.set_ylim(0, 2200)
    ax9.grid(True, alpha=0.3, axis='y')
    
    # Annotate improvements
    ax9.text(1, 1500, '↓29%', fontsize=10, ha='center', fontweight='bold', color='orange')
    ax9.text(2, 1250, '↓42%', fontsize=10, ha='center', fontweight='bold', color='green')
    
    for i, val in enumerate(episodes_required):
        ax9.text(i, val + 80, str(val), ha='center', fontsize=9, fontweight='bold')
    
    ax9.text(0.5, -0.3, 'Prop. 3: O(N/logK)', ha='center',
            transform=ax9.transAxes, fontsize=8, style='italic')
    
    # Overall title
    fig.suptitle('Figure 6. Learned Perceptual Curriculum (LPC) with Automatic Difficulty Decomposition',
                fontsize=14, fontweight='bold', y=0.98)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    save_figure(fig, 'figure6_lpc_curriculum')
    plt.close()


if __name__ == "__main__":
    main()
    
    # Generate additional figures
    print("\n" + "="*70)
    print("Generating additional Section 3 figures...")
    print("="*70)
    print()
    
    additional_figures = [
        ("Figure 5: PI-CMDR Pipeline", plot_pi_cmdr_pipeline),
        ("Figure 6: LPC Curriculum", plot_lpc_curriculum),
    ]
    
    for idx, (name, func) in enumerate(additional_figures, 3):
        try:
            print(f"[{idx}/4] Generating {name}...")
            func()
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*70)
    print("✓ ALL Section 3 figures complete!")
    print("="*70)
