# PreserveMy.World - Week 1 3D Reconstruction Research
**Prepared by:** Muhammad Zubair Ilyas

## Method Comparisons for PMW

### 1. COLMAP / Photogrammetry
* **Inputs:** A sequence of overlapping 2D digital images or video frames.
* **Outputs:** 3D Point Clouds, Camera Positions, and Mesh geometry.
* **Hardware Needs:** Medium CPU/RAM; Nvidia GPU with CUDA is preferred but can run basic sets locally.
* **Difficulty:** Medium.
* **PMW Fit:** Excellent for capturing high-fidelity architectural or outdoor environments from standard camera photography.

### 2. Neural Radiance Fields (NeRF)
* **Inputs:** Volumetric 2D images accompanied by precise camera tracking matrices.
* **Outputs:** A continuous volumetric scene function (highly detailed synthetic view generation).
* **Hardware Needs:** High; demands dedicated VRAM (Nvidia RTX GPUs) or Cloud GPUs (Google Colab).
* **Difficulty:** High.
* **PMW Fit:** Great for preserving complex objects with reflective surfaces or fine lighting details that traditional meshes struggle to render.

### 3. 3D Gaussian Splatting (3DGS)
* **Inputs:** Multi-view photos (often initialized with a sparse point cloud from COLMAP).
* **Outputs:** A collection of millions of 3D Gaussians that render rapidly in real-time.
* **Hardware Needs:** High for training (GPU required), but very lightweight and fast for web browsers to display.
* **Difficulty:** High.
* **PMW Fit:** The absolute best fit for interactive real-time web portfolios because users can rotate high-quality 3D models smoothly in a browser.

### 4. Monocular Depth Estimation
* **Inputs:** A single individual 2D image.
* **Outputs:** A 2D greyscale depth map (mapping close pixels to white, far pixels to black).
* **Hardware Needs:** Low; runs easily on standard consumer laptops or basic Python environments.
* **Difficulty:** Low.
* **PMW Fit:** Highly useful for rapid preview generation or giving a fast pseudo-3D parallax effect to a single asset photo uploaded by a user.