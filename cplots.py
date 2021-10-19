import os
import glob
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class cplots():

    def __init__(self):
        self.default_args()

    def default_args(self):
        #################################
        self.filename = ""
        self.save_dir = ""
        #################################
        self.width = 20
        self.height = 16
        self.axes_label_size = 35
        self.tick_label_size = 35
        self.axes_label_padding = 35
        self.margins = False
        #################################
        self.x_label = ''
        self.y_label = ''
        self.z_label = ''
        self.x_scale = 1
        self.y_scale = 1
        self.z_scale = 1
        #################################
        self.linewidth = 6
        self.linestyle = '-'
        # self.major_tick_length = 5
        # self.major_tick_width = 3
        self.tick_label_padding = 15
        #################################
        self.xlims = np.nan
        self.ylims = np.nan
        #################################
        self.xlabel_rot = 0
        self.ylabel_rot = 0
        self.xtick_rot = 0
        self.ytick_rot = 0
        #################################
        self.title = False
        self.title_size = 35
        #################################
        self.vline = False
        self.vline_values = []
        self.vline_lw = []
        self.vline_color = []
        self.vline_style = []
        self.vline_size = 4
        #################################
        self.hline = False
        self.hline_values = []
        self.hline_lw = []
        self.hline_color = []
        self.hline_style = []
        self.hline_size = 4
        #################################
        self.major_tick_length = 5
        self.major_tick_width = 3
        #################################
        self.minor_ticks = False
        self.minor_tick_length = 2
        self.minor_tick_width = 1
        #################################
        self.major_grid = False
        self.major_grid_color = 'lightgrey'
        self.major_grid_style = '-'
        self.major_grid_width = 2
        #################################
        self.minor_grid = False
        self.minor_grid_color = 'lightgrey'
        self.minor_grid_style = '-'
        self.minor_grid_width = 0.3
        #################################
        self.xbins = np.nan
        self.ybins = np.nan
        #################################

    def set_kwargs(self, kwargs):
        self.filename = kwargs.get('filename', self.filename)
        self.save_dir = kwargs.get('save_dir', self.save_dir)

    def axis_setup(self):
        plt.rc('axes', labelsize=self.axes_label_size)
        plt.rc('xtick', labelsize=self.tick_label_size)
        plt.rc('ytick', labelsize=self.tick_label_size)

    def set_save_dir(self):
        if self.save_dir != "":
            if (self.save_dir[-1] != '/'):
                self.save_dir = self.save_dir + '/'
            self.create_dir(self.save_dir)

    def create_dir(self, dir_in):
        if (dir_in[-1] != '/'):
            dir_in = dir_in + '/'
        if not os.path.exists(dir_in):
            os.makedirs(dir_in)

    def clean_dir(self, dir_in):

        if (dir_in[-1] != '/'):
            dir_in = dir_in + '/'

        self.create_dir(dir_in)

        to_clear = dir_in + '*'
        files = glob.glob(to_clear)
        for f in files:
            os.remove(f)

    def set_xlims(self):
        if isinstance(self.xlims, list):
            if len(self.xlims) == 2:
                plt.xlim([self.xlims[0],self.xlims[-1]])

    def set_ylims(self):
        if isinstance(self.ylims, list):
            if len(self.ylims) == 2:
                plt.ylim([self.ylims[0],self.ylims[-1]])

    def set_vlines(self):
        if self.vline:
            ylims = plt.gca().axes.get_ylim()
            for ii in range(0, len(self.vline_values)):
                plt.vlines(x=self.vline_values[ii],ymin=ylims[0],ymax=ylims[-1],lw=self.vline_lw[ii],color=self.vline_color[ii],linestyle=self.vline_style[ii])

    def set_hlines(self):
        if self.hline:
            xlims = plt.gca().axes.get_xlim()
            for ii in range(0, len(self.hline_values)):
                plt.hlines(y=self.y_scale*self.hline_values[ii],xmin=xlims[0],xmax=xlims[-1],lw=self.hline_lw[ii],color=self.hline_color[ii],linestyle=self.hline_style[ii])

    def set_major_ticks(self):
        plt.gca().tick_params(which='major',length=self.major_tick_length, width=self.major_tick_width, direction='out')

    def set_major_grid(self):
        if self.major_grid:
            plt.grid(which='major',color=self.major_grid_color, linestyle=self.major_grid_style, linewidth=self.major_grid_width)


    # def set_major_minor(self):
    #     plt.gca().tick_params(which='major',length=self.major_tick_length, width=self.major_tick_width, direction='out')
    #     if self.minor_ticks:
    #         plt.gca().minorticks_on()
    #         plt.gca().tick_params(which='minor',length=self.minor_tick_length,width=self.minor_tick_length,direction='out')
    #     if self.major_grid:
    #         plt.grid(which='major',color=self.major_grid_color, linestyle=self.major_grid_style, linewidth=self.major_grid_width)
    #     if self.minor_grid:
    #         plt.grid(which='minor',color=self.minor_grid_color,linestyle=self.minor_grid_style,linewidth=self.minor_grid_width)

    ####################################
    ####################################
    ####################################

    def line_plot(self, x, data, *args, **kwargs):

        self.set_kwargs(kwargs)
        self.set_save_dir()
        self.axis_setup()

        y = np.array(data)

        plt.figure(figsize=(self.width, self.height))
        plt.ticklabel_format(useOffset=False)

        self.set_major_ticks()
        self.set_major_grid()

        self.set_xlims()
        self.set_ylims()

        if self.margins == False:
            plt.margins(x=0)

        plt.xlabel(self.x_label, labelpad=self.axes_label_padding, rotation=self.xlabel_rot)
        plt.ylabel(self.y_label, labelpad=self.axes_label_padding, rotation=self.ylabel_rot)

        plt.xticks(rotation=self.xtick_rot)
        plt.yticks(rotation=self.ytick_rot)

        if np.isnan(self.xbins) != True:
            plt.locator_params(axis='x', nbins=self.xbins)
            # plt.gca().xaxis.set_major_locator(plt.MaxNLocator(self.xbins))

        if np.isnan(self.ybins) != True:
            plt.gca().yaxis.set_major_locator(plt.MaxNLocator(self.ybins))

        if np.ndim(y) > 1:
            num = y.shape[0]
            for ii in range(0, num):
                plt.plot(x,y[ii,:],linewidth=self.linewidth)
        else:
            plt.plot(x,y,linewidth=self.linewidth)

        # self.set_ylabel(rotation=90)

        # myFmt = mdates.DateFormatter("%Y-%m-%d %H:%M:%S")
        # plt.gca().xaxis.set_major_formatter(myFmt)

        self.set_vlines()
        self.set_hlines()

        if self.title != False:
            plt.title(self.title, fontsize=self.title_size)

        plt.tight_layout()
        plt.savefig(self.save_dir+self.filename + ".png")

        # fig = plt.figure()
        # plt.clear()
        plt.close()
