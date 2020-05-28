# Passenger flows, backbone and robustness in subway networks

One of the 5 following modes should be chosen at the beginning of the code:
    
    - Basic: This mode computes all passenger flows through the network when neither the inputs nor the multilayer aspect of the network are considered.
    
    - BC: This is the default mode that computes all the passenger flows through the network when there are no failures. 
    
    - Backbone: This mode computes all the passenger flows through the network as well as the backbone that is obtained by combining 3 different filters. 
    
    - L14RERAFailure: This mode computes the passenger flows through the network when line 14 as well as the RERA fail at the same time.
    
    - DeconfinementPlan: This mode computes the passenger flows for the deconfinement plan of the RATP from may 2020.
