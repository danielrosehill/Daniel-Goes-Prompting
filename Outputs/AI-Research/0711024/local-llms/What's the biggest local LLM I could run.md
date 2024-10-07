# Prompt

I'm attaching my workstation spec for context. What's the largest local LLM I could currently run? Output part 2: I want to max out the spec on this system to make it run the largest LLM I possibly can. What mods to I make, how much they cost, and what LLM can I run now?

# Output

### Part 1: **Current LLM Capability Based on Your Workstation**

Based on the specifications of your current system, here’s an analysis of what the largest local LLM you could realistically run is:

#### **Workstation Specs**:
- **CPU**: Intel Core i7-12700F (12 cores / 20 threads)
- **GPU**: AMD Radeon RX 7700 XT with 12GB VRAM
- **RAM**: 32GB DDR5 4800 MHz
- **Storage**: 2.73TB total storage, using RAID1, with around 2.5TB unallocated space.
- **OS**: Fedora Workstation 40

#### **Current LLM Capability**:
With **32GB of RAM** and a **12GB VRAM GPU**, you are somewhat limited to **small to medium-sized models**. Based on this, you could comfortably run models in the **7B-13B parameter range**. The larger models, like **LLaMA-7B** or **GPT-NeoX-6B**, would fit well within these limits. However, you would likely struggle with anything above 13B parameters without performance degradation due to VRAM and RAM constraints.

#### **Examples of Models You Could Run Now**:
- **LLaMA-7B**: Known for its efficiency, you can run this model smoothly with 12GB of VRAM and 32GB of system RAM.
- **GPT-NeoX-6B**: This model is also well-suited for your specs, given its balance between power and resource needs.
- **GPT-J (6B)**: This would run efficiently as well.
  
If you use quantization (e.g., 4-bit or 8-bit), you can push these models even further and possibly try out models up to 13B parameters.

---

### Part 2: **Maxing Out Your Workstation for Larger LLMs**

To handle **even larger LLMs**, you would need to focus on upgrading two main components: **GPU** and **RAM**. Here’s what you can do:

#### **1. RAM Upgrade**:
Upgrading to **64GB or 128GB** of RAM will give you significantly more room for running larger models, especially if you start pushing the system with high-throughput batch processing.

- **Upgrade Cost**:
  - **64GB DDR5** (2x32GB, 4800 MHz): ~$200 - $300
  - **128GB DDR5** (4x32GB, 4800 MHz): ~$450 - $600

#### **2. GPU Upgrade**:
Your GPU with 12GB of VRAM is limiting when it comes to very large LLMs (30B+ parameters). Upgrading to a **24GB VRAM GPU** (like the NVIDIA RTX 3090 or RTX 4090) will allow you to run models up to **30B parameters**.

- **Upgrade Cost**:
  - **NVIDIA RTX 3090** (24GB VRAM): ~$1,500 - $1,800
  - **NVIDIA RTX 4090** (24GB VRAM): ~$1,600 - $2,000

#### **3. Storage**:
You have enough storage for models and processing data, especially with around 2.5TB free. If you want to optimize further, adding a **high-speed NVMe drive** can speed up data handling, though it's not crucial unless you're handling massive datasets.

- **Upgrade Cost**: 
  - **Additional NVMe SSD (2TB)**: ~$150 - $250

---

### **LLMs You Could Run After Upgrades**:

After upgrading your RAM and GPU, you could comfortably run **larger models** in the **20B-30B** range, including:
- **GPT-NeoX-20B**: A larger open-source model that requires more VRAM and system RAM.
- **LLaMA-30B**: With 24GB VRAM and 128GB system RAM, this model would run more comfortably.

### Total Estimated Cost for Maxing Out:
- **64GB RAM upgrade**: ~$300
- **RTX 3090/4090 upgrade**: ~$1,800
- **Optional storage upgrade (2TB NVMe SSD)**: ~$200

**Total Cost**: ~$2,300 for maximum upgrades that would allow you to run models up to 30B parameters efficiently.

 