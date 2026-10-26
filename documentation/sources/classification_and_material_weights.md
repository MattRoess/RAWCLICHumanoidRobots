[
  {
    "class_id": "HRC-1",
    "class_name": "Industrial Workhorse",
    "definition": "Bipedal humanoid robots designed for operational deployment in structured industrial environments like manufacturing, logistics, and warehousing [1, 2]. Key criteria include high payload capacity (typically ≥ 20 kg), long operational runtime (often with swappable batteries), robust construction for safety and durability, and AI systems geared towards task execution and repetition [3, 5, 8, 11].",
    "representative_examples": [
      "Figure 02",
      "Apptronik APOLLO",
      "Sanctuary AI Phoenix",
      "UBTECH Robotics Walker S"
    ],
    "specifications": {
      "total_weight_kg": "70 - 73 [3, 8, 11]",
      "degrees_of_freedom_total": "40 - 50+ [14]",
      "payload_kg": "20 - 25 [3, 8, 11]",
      "battery_capacity_kWh": "1.2 - 2.3 [9, 14]",
      "runtime_hours": "4 - 5 [3, 8]"
    },
    "material_weight_breakdown": {
      "components": [
        {
          "component": "Structural Frame & Chassis",
          "min_kg": 18.0,
          "mode_kg": 21.0,
          "max_kg": 25.0
        },
        {
          "component": "Actuators & Drivetrain",
          "min_kg": 20.0,
          "mode_kg": 23.0,
          "max_kg": 26.0
        },
        {
          "component": "Battery System",
          "min_kg": 10.0,
          "mode_kg": 12.0,
          "max_kg": 15.0
        },
        {
          "component": "Shell, Casing & Textiles",
          "min_kg": 4.0,
          "mode_kg": 6.0,
          "max_kg": 8.0
        },
        {
          "component": "Electronics, Sensors & Wiring [23, 24, 25, 26]",
          "min_kg": 5.0,
          "mode_kg": 7.0,
          "max_kg": 9.0
        }
      ],
      "materials": [
        {
          "material": "Aluminum & Magnesium Alloys [18, 20]",
          "min_kg": 15.0,
          "mode_kg": 18.0,
          "max_kg": 22.0
        },
        {
          "material": "Titanium & Steel Alloys [18]",
          "min_kg": 5.0,
          "mode_kg": 8.0,
          "max_kg": 12.0
        },
        {
          "material": "High-Performance Polymers (PEEK, PPS, etc.) [19, 20, 21, 22]",
          "min_kg": 3.0,
          "mode_kg": 5.0,
          "max_kg": 8.0
        },
        {
          "material": "Composites (CFRP) [22]",
          "min_kg": 2.0,
          "mode_kg": 4.0,
          "max_kg": 6.0
        },
        {
          "material": "Elastomers & Soft Materials (Silicone, TPE) [20, 21]",
          "min_kg": 1.0,
          "mode_kg": 2.0,
          "max_kg": 3.0
        }
      ]
    }
  },
  {
    "class_id": "HRC-2",
    "class_name": "Dynamic Research Platform",
    "definition": "Advanced bipedal robots developed to explore and push the boundaries of locomotion, agility, and dynamic control [1, 2]. Characterized by exceptional mobility (e.g., running, jumping), complex high-power actuation systems (electric or hydraulic), and are primarily utilized in research and development settings rather than for immediate commercial application [6, 7].",
    "representative_examples": [
      "Boston Dynamics Atlas",
      "Unitree H1",
      "Ti5 Robotics Yao Guang"
    ],
    "specifications": {
      "total_weight_kg": "47 - 89 [6, 14, 16]",
      "degrees_of_freedom_total": "28 - 45 [6, 14]",
      "payload_kg": "Not Emphasized",
      "battery_capacity_kWh": "0.8 - 1.2 [14, 15]",
      "runtime_hours": "Varies / Short"
    },
    "material_weight_breakdown": {
      "components": [
        {
          "component": "Structural Frame & Chassis",
          "min_kg": 12.0,
          "mode_kg": 15.0,
          "max_kg": 25.0
        },
        {
          "component": "Actuators & Drivetrain",
          "min_kg": 15.0,
          "mode_kg": 20.0,
          "max_kg": 35.0
        },
        {
          "component": "Battery System [24]",
          "min_kg": 5.0,
          "mode_kg": 7.0,
          "max_kg": 10.0
        },
        {
          "component": "Shell, Casing & Textiles",
          "min_kg": 2.0,
          "mode_kg": 3.0,
          "max_kg": 5.0
        },
        {
          "component": "Electronics, Sensors & Wiring [25, 26]",
          "min_kg": 4.0,
          "mode_kg": 6.0,
          "max_kg": 8.0
        }
      ],
      "materials": [
        {
          "material": "Aluminum & Magnesium Alloys [6, 18]",
          "min_kg": 10.0,
          "mode_kg": 15.0,
          "max_kg": 25.0
        },
        {
          "material": "Titanium & Steel Alloys [6, 18]",
          "min_kg": 8.0,
          "mode_kg": 12.0,
          "max_kg": 20.0
        },
        {
          "material": "High-Performance Polymers (PEEK, PPS, etc.) [19, 20]",
          "min_kg": 2.0,
          "mode_kg": 4.0,
          "max_kg": 6.0
        },
        {
          "material": "Composites (CFRP) [22]",
          "min_kg": 4.0,
          "mode_kg": 7.0,
          "max_kg": 10.0
        },
        {
          "material": "Elastomers & Soft Materials (Silicone, TPE)",
          "min_kg": 0.5,
          "mode_kg": 1.0,
          "max_kg": 2.0
        }
      ]
    }
  },
  {
    "class_id": "HRC-3",
    "class_name": "Service & Interaction Robot",
    "definition": "Humanoid robots designed primarily for direct interaction with people in service, entertainment, or domestic roles [1, 2]. They prioritize safety, advanced human-robot interaction (HRI) capabilities such as expressive faces and natural language processing, and navigation in public or home environments [14]. Payload and power are secondary to interaction quality.",
    "representative_examples": [
      "Engineered Arts Ameca",
      "UBTECH Robotics Walker (Personal Assistant)",
      "SoftBank Pepper"
    ],
    "specifications": {
      "total_weight_kg": "30 - 60",
      "degrees_of_freedom_total": "20 - 40",
      "payload_kg": "1 - 5 [14]",
      "battery_capacity_kWh": "0.6 - 1.0",
      "runtime_hours": "3 - 12"
    },
    "material_weight_breakdown": {
      "components": [
        {
          "component": "Structural Frame & Chassis",
          "min_kg": 8.0,
          "mode_kg": 12.0,
          "max_kg": 18.0
        },
        {
          "component": "Actuators & Drivetrain",
          "min_kg": 8.0,
          "mode_kg": 12.0,
          "max_kg": 16.0
        },
        {
          "component": "Battery System",
          "min_kg": 4.0,
          "mode_kg": 6.0,
          "max_kg": 8.0
        },
        {
          "component": "Shell, Casing & Textiles",
          "min_kg": 5.0,
          "mode_kg": 8.0,
          "max_kg": 12.0
        },
        {
          "component": "Electronics, Sensors & Wiring",
          "min_kg": 4.0,
          "mode_kg": 6.0,
          "max_kg": 8.0
        }
      ],
      "materials": [
        {
          "material": "Aluminum & Magnesium Alloys",
          "min_kg": 5.0,
          "mode_kg": 10.0,
          "max_kg": 15.0
        },
        {
          "material": "Titanium & Steel Alloys",
          "min_kg": 1.0,
          "mode_kg": 3.0,
          "max_kg": 5.0
        },
        {
          "material": "High-Performance Polymers (PC/ABS, PA, etc.) [19, 21]",
          "min_kg": 6.0,
          "mode_kg": 10.0,
          "max_kg": 14.0
        },
        {
          "material": "Composites (CFRP)",
          "min_kg": 0.0,
          "mode_kg": 1.0,
          "max_kg": 3.0
        },
        {
          "material": "Elastomers & Soft Materials (Silicone, TPE) [20, 21]",
          "min_kg": 2.0,
          "mode_kg": 4.0,
          "max_kg": 6.0
        }
      ]
    }
  },
  {
    "class_id": "HRC-4",
    "class_name": "Lightweight & Educational Platform",
    "definition": "Relatively smaller and lighter humanoid robots created as versatile and often more affordable platforms for education, academic research, and hobbyist applications [1, 2]. They feature moderate capabilities, are programmable, and focus on accessibility for learning and development in robotics and AI.",
    "representative_examples": [
      "Xiaomi CyberOne",
      "Unitree G1",
      "SoftBank NAO"
    ],
    "specifications": {
      "total_weight_kg": "5 - 55 [14]",
      "degrees_of_freedom_total": "21 - 43 [14]",
      "payload_kg": "1.5 - 10 [14]",
      "battery_capacity_kWh": "Not specified",
      "runtime_hours": "1 - 3"
    },
    "material_weight_breakdown": {
      "components": [
        {
          "component": "Structural Frame & Chassis",
          "min_kg": 2.0,
          "mode_kg": 8.0,
          "max_kg": 15.0
        },
        {
          "component": "Actuators & Drivetrain",
          "min_kg": 2.0,
          "mode_kg": 10.0,
          "max_kg": 18.0
        },
        {
          "component": "Battery System",
          "min_kg": 0.5,
          "mode_kg": 3.0,
          "max_kg": 6.0
        },
        {
          "component": "Shell, Casing & Textiles",
          "min_kg": 1.0,
          "mode_kg": 5.0,
          "max_kg": 10.0
        },
        {
          "component": "Electronics, Sensors & Wiring",
          "min_kg": 0.5,
          "mode_kg": 4.0,
          "max_kg": 8.0
        }
      ],
      "materials": [
        {
          "material": "Aluminum & Magnesium Alloys [18]",
          "min_kg": 1.0,
          "mode_kg": 5.0,
          "max_kg": 12.0
        },
        {
          "material": "Titanium & Steel Alloys",
          "min_kg": 0.0,
          "mode_kg": 1.0,
          "max_kg": 4.0
        },
        {
          "material": "High-Performance Polymers (PC/ABS, PA, etc.) [19, 21]",
          "min_kg": 3.0,
          "mode_kg": 10.0,
          "max_kg": 20.0
        },
        {
          "material": "Composites (CFRP)",
          "min_kg": 0.0,
          "mode_kg": 2.0,
          "max_kg": 5.0
        },
        {
          "material": "Elastomers & Soft Materials (Silicone, TPE)",
          "min_kg": 0.2,
          "mode_kg": 1.0,
          "max_kg": 2.0
        }
      ]
    }
  }
]
## References
1. Types of Humanoid Robots: 15 Examples - PROVEN Robotics. (n.d.). Retrieved from https://provenrobotics.ai/types-of-humanoid-robots/
2. Humanoid Robots Guide (2025): ... - Top 3D Shop. (n.d.). Retrieved from https://top3dshop.com/blog/humanoid-robots-types-history-best-models
3. QVIRO | Apptronik APOLLO Specifications. (n.d.). Retrieved from https://qviro.com/product/apptronik/apollo/specifications
4. Apollo - Humanoid.guide. (n.d.). Retrieved from https://humanoid.guide/product/apollo/
5. Apollo - Apptronik. (n.d.). Retrieved from https://apptronik.com/apollo
6. QVIRO | Boston Dynamics Atlas Specifications. (n.d.). Retrieved from https://qviro.com/product/boston-dynamics/atlas/specifications
7. Atlas (robot) - Wikipedia. (n.d.). Retrieved from https://en.wikipedia.org/wiki/Atlas_(robot)
8. QVIRO | Figure Figure 02 Specifications. (n.d.). Retrieved from https://i.ytimg.com/vi/0SRVJaOg9Co/sddefault.jpg
9. Figure 02 - Humanoid.guide. (n.d.). Retrieved from https://humanoid.guide/product/figure-02/
10. Figure steps closer to humanoid robots... - New Atlas. (n.d.). Retrieved from https://newatlas.com/robotics/figure-02-humanoid-robot-launch/
11. QVIRO | Sanctuary AI Phoenix Specifications. (n.d.). Retrieved from https://qviro.com/product/sanctuary-ai/phoenix/specifications
12. Sanctuary AI Phoenix Review - Robozaps Blog. (n.d.). Retrieved from https://blog.robozaps.com/b/sanctuary-ai-phoenix-review
13. Sanctuary AI unveils Phoenix... - Sanctuary.ai Blog. (n.d.). Retrieved from https://www.sanctuary.ai/blog/sanctuary-ai-unveils-phoenix-a-humanoid-general-purpose-robot-designed-for-work
14. QVIRO | Unitree H1 Specifications. (n.d.). Retrieved from https://qviro.com/product/unitree/h1/specifications
15. Unitree H1 - Unitree Website. (n.d.). Retrieved from https://www.unitree.com/h1/
16. Unitree H1 Review - Robozaps Blog. (n.d.). Retrieved from https://blog.robozaps.com/b/unitree-h1-review
17. Unitree H1 Humanoid Robot - RobotsGuide. (n.d.). Retrieved from https://robotsguide.com/robots/unitree-h1
18. Advanced materials for humanoid robots - Goodfellow. (n.d.). Retrieved from https://www.goodfellow.com/usa/resources/advanced-materials-for-humanoid-robots/
19. Plastics for humanoid robots - peekchina.com. (n.d.). Retrieved from https://www.peekchina.com/blog/plastics-for-humanoid-robots.html
20. The new material revolution of humanoid robots - sbfchem.com. (n.d.). Retrieved from https://www.sbfchem.com/index.php/news/1009/The_new_material_revolution_of_humanoid_robots.html
21. Advanced materials for humanoid robots - taifengfr.com. (n.d.). Retrieved from https://www.taifengfr.com/news/advanced-materials-for-humanoid-robots/
22. Application and development analysis of compos... - cmag.com.cn. (n.d.). Retrieved from https://www.cmag.com.cn/news/application-and-development-analysis-of-compos-85160017.html
23. PMC article PMC12829565. (n.d.). Retrieved from https://pmc.ncbi.nlm.nih.gov/articles/PMC12829565/
24. Building a Humanoid Robot... - thinkrobotics.com. (n.d.). Retrieved from https://thinkrobotics.com/blogs/tutorials/building-a-humanoid-robot-step-by-step-engineering-guide-for-beginners
25. Weighing Technology in AI-Powered Humanoid Robots... - weighingreview.com. (n.d.). Retrieved from https://www.weighingreview.com/article/weighing-technology-in-ai-powered-humanoid-robots-enhancing-balance-perception-and-interaction
26. PMC article PMC10007397. (n.d.). Retrieved from https://pmc.ncbi.nlm.nih.gov/articles/PMC10007397/
27. Humanoid robot - Wikipedia. (n.d.). Retrieved from https://en.wikipedia.org/wiki/Humanoid_robot