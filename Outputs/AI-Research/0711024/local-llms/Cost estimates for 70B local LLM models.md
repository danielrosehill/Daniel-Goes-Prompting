# Prompt

I see some people in the various LLM subs on Reddit talking about running 70B parameter models locally. What kind of hardware do you think these guys are running and how much do you think those builds cost?

# Output

Running 70B parameter models locally is quite a challenge and requires high-end hardware configurations. Here’s a breakdown of the typical specifications needed to handle such large models and an estimated cost for those builds:

### Hardware Requirements for 70B Parameter Models:

1. **GPU**:
   - **Type**: High-end NVIDIA GPUs are the go-to choice for running large models due to their VRAM capacity and CUDA support.
   - **VRAM Needed**: At least **48GB VRAM** per GPU, as large models like the **70B parameter** models typically require multiple GPUs or GPUs with substantial VRAM.
   - **Example GPUs**:
     - **NVIDIA A6000**: 48GB VRAM, designed for AI workloads.
     - **NVIDIA H100**: 80GB or 96GB VRAM, cutting-edge performance but very expensive.

2. **RAM**:
   - **System RAM**: At least **128GB** or **256GB** of system RAM is recommended to handle the model's memory overhead and support concurrent processing tasks.

3. **CPU**:
   - **Type**: A powerful multi-core CPU to handle the data processing and model management.
   - **Examples**:
     - **AMD Ryzen Threadripper PRO**: 64 cores.
     - **Intel Xeon Scalable Processors**: Options with high core counts.

4. **Motherboard**:
   - A workstation motherboard that can support multiple GPUs and has adequate slots for RAM.
   - Example: **Supermicro X11SPA-T** for Intel Xeon CPUs or equivalent for AMD.

5. **Storage**:
   - High-speed NVMe SSDs for model storage and data handling. You might need **several terabytes** of fast storage.
   - Example: **2TB NVMe SSDs**, RAID configurations for speed and redundancy.

6. **Cooling and Power Supply**:
   - A robust cooling solution to manage heat from multiple GPUs.
   - A high-capacity power supply (e.g., **1200W - 1600W**) to support multiple GPUs.

### Estimated Costs:

- **GPUs**:
  - **NVIDIA A6000**: ~$5,000 each. You would typically need **at least two** for a 70B model.
  - **NVIDIA H100**: ~$30,000+ each, which would be used in fewer setups due to the high cost.
  
- **RAM**:
  - **128GB DDR5**: ~$400 - $600.
  - **256GB DDR5**: ~$1,200 - $1,500.

- **CPU**:
  - **AMD Ryzen Threadripper PRO**: ~$2,000 - $4,000 depending on the model.
  - **Intel Xeon Scalable**: ~$3,000 - $5,000 depending on the configuration.

- **Motherboard**:
  - High-end workstation motherboard: ~$300 - $600.

- **Storage**:
  - **NVMe SSDs (2TB)**: ~$150 - $250 each. You might want **4TB or more** total, leading to around **$600 - $1,000** for multiple drives.

- **Cooling and PSU**:
  - High-performance cooling: ~$200 - $500.
  - Power Supply: ~$300 - $500.

### **Total Estimated Cost**:
Depending on the GPU choice and system configuration, the total cost for a build capable of running 70B models can vary significantly:

- **Mid-Range Setup** (Two A6000 GPUs):
  - **Total**: ~$15,000 - $25,000.

- **High-End Setup** (One H100 GPU):
  - **Total**: ~$35,000 - $50,000+.

### Summary:
The users you see running 70B parameter models locally are likely utilizing high-end workstation setups that can cost upwards of **$15,000 to $50,000**, depending on the specific components they choose. This includes multiple high-VRAM GPUs, substantial RAM, powerful CPUs, and other supporting hardware. 

If you have further questions about specific components or need assistance on building such a system, feel free to ask!