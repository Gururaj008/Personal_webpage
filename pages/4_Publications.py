import streamlit as st
import webbrowser 
from PIL import Image

def paper1_link():
    link = "https://link.springer.com/chapter/10.1007/978-981-16-1642-6_30"
    webbrowser.open(link)

def paper2_link():
    link = "https://link.springer.com/chapter/10.1007/978-981-16-1642-6_11"
    webbrowser.open(link)

def paper3_link():
    link = "https://link.springer.com/chapter/10.1007/978-981-16-1642-6_14"
    webbrowser.open(link)

def paper4_link():
    link = "https://ieeexplore.ieee.org/document/8978331"
    webbrowser.open(link)

def paper5_link():
    link = "https://www.ijrte.org/wp-content/uploads/papers/v8i3/C5139098319.pdf"
    webbrowser.open(link)


def paper6_link():
    link = "https://ijamtes.org/VOL-9-ISSUE-03-2019-1/"
    webbrowser.open(link)











if __name__ == '__main__':
    col101, col102, col103 = st.columns([8,8,8])
    with col102:
        st.subheader(':orange[Publications]')
    st.write('')
    st.write('')
    st.markdown(':orange[**Self-Sustaining Community for a Green Future—A Case Study**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> India is one of the fastest growing economies in the world and the demand for energy is ever increasing. Traditionally, the majority of the energy demand in India is met by fossil fuels. India, being the second most populous country in the world naturally the demand for automobiles is high. The reliance on fossil fuels for generating electricity coupled with large number of automobiles contributes heavily toward emission of greenhouse gases, thereby polluting the air in most of the metropolitan cities. To overcome the reliance on fossil fuels, the past decade saw heavy investments being made by both government and private sector to generate clean and green energy using renewable sources like solar and wind energy. Today, India is the fastest growing renewable energy market in the world. In order to tackle the emissions from vehicles, the government has adopted many policies to encourage the buying and usage of electric vehicles (EV). The electric vehicle, can be “truly non-polluting” only if the energy that is used to charge the battery is generated from a non-polluting source like solar or wind energy. If everyone in the country switches to EVs, the greenhouse gases emissions and the resulting air pollution would drastically come down. On the contrary, it may turn out to be very difficult to generate and supply the amount of energy needed to charge all those EVs. Hence, it calls for distributed generation at the community level. The climate in most parts of India is very conducive for generating electricity using solar energy and some parts of the country receive adequate solar and wind energy, one such place is Chitradurga, Karnataka. This paper proposes generation of electricity using solar photovoltaic (PV) panels and vertical axis wind turbines (VAWT) placed on the rooftop of the building to meet both household and vehicular energy demand of the occupants. Making the community completely self-sustained and contributing to a green future.  </div>', unsafe_allow_html=True)
    st.write('')
    col11, col12, col13 = st.columns([2,8,2])
    with col12:
        st.button("Self-Sustaining Community for a Green Future—A Case Study", on_click= paper1_link,key=1)
    st.divider()

    st.markdown(':orange[**Digital Twinning of the Battery Systems—A Review**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> The share of renewable energy in the grid is ever increasing. Whenever excess energy is generated, it can be stored in large-scale battery systems to support the grid during peak loads, nullifying the need for gas/diesel power plants. Battery storage is remodelling the global electric grid and is a key element for the shift to sustainable energy. In order to extract optimum performance and to ensure reliable, safe working of battery system, its constant monitoring is a must.Digital twin architecture of the battery system offers digital services to different stakeholders starting from the manufacturing through its secondary usage until the end of its life. Digital twin helps in bridging the gap and offers an innovative approach for both manufacturing and usage of the product. This paper focuses on reviewing different architecture of digital twins along with communication protocols, thus providing readers with an insight into recent trends in digital twin architecture for the battery system.  </div>', unsafe_allow_html=True)
    st.write('')
    col14, col15, col16 = st.columns([2,8,2])
    with col15:
        st.button("Digital Twinning of the Battery Systems—A Review", on_click= paper2_link,key=2)
    st.divider()

    st.markdown(':orange[**Electrical Field and Potential Distribution Simulation of 220 kV Porcelain String Insulator Using COMSOL Multiphysics**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> Fidelity of the network and its equipment is imperative for the performance of electrical power system. Electrical energy from generating station is transmitted through high-voltage lines to the load centres. Insulators are used to both support as well as separate the conductors at high voltage. They are designed to withstand not only just typical voltages but also over-voltages by the virtue of switching events or lightning effect besides environmental stresses like snow, rain, pollution. Insulators employed to transmit/distribute the electric power are usually made up of ceramic/glass/polymer material. When the local electric field on the surface of high-voltage insulator is greater than the ambient air’s ionization value it leads to the discharge activity. Environmental conditions like rain, fog, pollution along with the high voltage affect the electric field. Electric field grading techniques can be used to better design the insulators provided the electric field on the surface of the insulator is known. Surface flashover may occur on the ceramic insulators when the applied electric field is high enough. Consequently, grading devices are required to keep the electric field under acceptable levels. Objective of the aforementioned research is to study the electric field and potential distribution (EFPD) along the ceramic insulators. Firstly, under clean/dry conditions and then under various levels of Sodium Chloride (NaCl) pollution using finite element method. The computer simulations are realized using commercially available CATIA and COMSOL multiphysics software packages. The simulation results obtained are presented and analysed.  </div>', unsafe_allow_html=True)
    st.write('')
    col14, col15, col16 = st.columns([2,8,2])
    with col15:
        st.button("Electrical Field and Potential Distribution Simulation of 220 kV Porcelain String Insulator Using COMSOL Multiphysics", on_click= paper3_link,key=3)
    st.divider()

    st.markdown(':orange[**Hybrid Power Generation on top of the Vehicle**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> India is blessed with more than 300 days of bright sunshine and a large road network. Least amount of obstruction for sunshine and wind flow will be present in the highway. In this Paper, the prospect of utilizing the available solar and wind energy is explored. Millions of buses and trucks will be travelling on the highway in India on any given day, they can be used for converting solar and wind energy into useful electrical energy. A combination of permanent magnet synchronous generator and vertical axis wind turbine is placed inside a channel on vehicle top portion. Vehicle can have n number of such channels depending upon dimensions of the turbine and width of the vehicle. When the vehicle travels on the highway, the combination can generate electricity. On top of these channels, flexible solar panels are placed which also generate electricity. The generated electricity from hybrid source is stored in the battery bank. Once the vehicle reaches its destination, the energy stored can be utilized to provide plug and play battery to run an electric scooter or can be fed to grid by converting into alternating current or may even be utilized to satisfy local energy demand in the vehicle like an air conditioner.  </div>', unsafe_allow_html=True)
    st.write('')
    col14, col15, col16 = st.columns([2,8,2])
    with col15:
        st.button("Hybrid Power Generation on top of the Vehicle", on_click= paper4_link,key=4)
    st.divider()

    st.markdown(':orange[**Wind Energy Conversion System for a Moving Vehicle**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> India has the second largest road network in the world. Since the highway is wide open space there will not be any obstruction for the wind flow. When the vehicle is moving at a faster rate on a highway, the velocity of the wind on top of the vehicle will be high, which can be used to produce electricity. In this work, the possibility of harnessing wind energy on the top of a moving vehicle is proposed. According to the statistics, in India approximately 0.2 million buses & even more number of trucks will be plying on any given day. These vehicles can be used for generation of electricity by using a Wind Energy Conversion System .The vehicle is fitted with a chamber for airflow, chamber is further divided into channels. Each channel has a Vertical Axis Wind Turbine (VAWT) coupled to a Permanent Magnet Synchronous Generator (PMSG), generating electricity and charging the battery bank. This stored energy can be used to run local loads such as the Air conditioner, instantaneously improving the fuel economy of the vehicle in turn reducing the carbon emission. For a non air conditioned vehicle, upon reaching the destination energy stored in the battery bank can be converted to AC and fed to the grid or can be used to run an e-scooter as plug & play battery thus promoting the use of e-vehicles. </div>', unsafe_allow_html=True)
    st.write('')
    col14, col15, col16 = st.columns([2,8,2])
    with col15:
        st.button("Wind Energy Conversion System for a Moving Vehicle", on_click= paper5_link,key=5)
    st.divider()

    st.markdown(':orange[**A STUDY OF SOLAR PV SYSTEM AT DISTRICT LEVEL & ITS IMPLICATIONS**]')
    st.write('')
    st.markdown('<div style="text-align: justify"> India\’s economy is on a fast track in the past decade & is one of the fastest growing in the world.With this growth rate the energy demand is only going to increase multiple folds in the coming years. The electricity demand during the period 1997-2019 grew by 5.7% per year and from 2020-2047 it is expected to grow by 3.9% per year. Major electricity demand in an urban scenario is from educational institutions, hospitals, banks, government buildings etc. apart from residential buildings. So the installation of rooftop solar PV systems on these buildings will not only reduce the electricity demand from the supplier also solar being eco friendly will reduce the carbon footprint of the country. In this paper we have studied the feasibility of installing solar PV systems on educational institutions, hospitals, banks, government buildings etc. Along with investment cost, returns, payback period, breakeven point & the environmental impact.  </div>', unsafe_allow_html=True)
    st.write('')
    col14, col15, col16 = st.columns([2,8,2])
    with col15:
        st.button("A STUDY OF SOLAR PV SYSTEM AT DISTRICT LEVEL & ITS IMPLICATIONS", on_click= paper6_link,key=6)
    st.divider()

    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    col901, col902, col903 = st.columns(3)
    with col903:
        st.markdown('_An_ _effort_ _by_ : :blue[**MAVERICK_GR**]')