import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 50)

phi, theta = np.meshgrid(phi, theta)

phi_plane = [0, np.pi]

phi_plane, theta_plane = np.meshgrid(phi_plane, theta)

def calc_Rad_Dia(l):
    
    r = (np.cos(np.pi*l*np.cos(theta))-np.cos(np.pi*l))/np.sin(theta)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x,y,z

def calc_Plane_RD(l):
    
    r = (np.cos(np.pi*l*np.cos(theta_plane))-np.cos(np.pi*l))/np.sin(theta_plane)

    x = r * np.sin(theta_plane) * np.cos(phi_plane)
    y = r * np.sin(theta_plane) * np.sin(phi_plane)
    z = r * np.cos(theta_plane)
    return x,z

def plot_Rad_Dia(x,y,z,ax,l):
    ax.plot_surface(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Gráfico de diagrama de radiación para l={l}')
    return ax

def ani_Rad_Dia(fig,ax,l):
    
    def update(frame):
        ax.clear()  # Limpiar el eje en cada iteración
        x, y, z = calc_Rad_Dia(l[frame])
        ax.plot_surface(x, y, z)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Gráfico de diagrama de radiación para l={l[frame]}')
        fig.savefig(f'./Imagenes3D/Long_{l[frame]}_lambda.png')
        return ax

    return FuncAnimation(fig, update, frames=len(l), interval=200)

def plot_Plane_RD(x,z,ax,l):
    ax.plot(x, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_title(f'Gráfico de diagrama de radiación para l={l}')
    return ax

def ani_Plane_RD(fig,ax,l):
    
    def update(frame):
        ax.clear()  # Limpiar el eje en cada iteración
        x, z = calc_Plane_RD(l[frame])
        ax.plot(x, z)
        ax.set_xlabel('X')
        ax.set_ylabel('Z')
        ax.set_title(f'Gráfico de diagrama de radiación para l={l[frame]}')
        fig.savefig(f'./Imagenes2D/Long_{l[frame]}_lambda.png')
        return ax

    return FuncAnimation(fig, update, frames=len(l), interval=200)
