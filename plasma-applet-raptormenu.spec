%define version  0.0
%define git git20090309
%define release  %mkrel 0.%git.2
%define oname    raptor

%define libnamedev %mklibname %{name} -d

Name:		 plasma-applet-%oname
Version:	 %{version}
Release:	 %{release}
License:	 GPLv2+
Url:		 http://www.raptor-menu.org
Epoch:       1
Group:		 Graphical desktop/KDE
Source0:	 %{oname}-%version.%git.tar.bz2
Summary:         Plasmoid Menu for KDE4
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:   cmake >= 2.4.5
BuildRequires:   kdelibs4-devel
BuildRequires:   kdebase4-workspace-devel
Requires:        kdebase4-runtime
Requires:        plasma-engine-raptor
Provides:        plasma-applet

%description -n plasma-applet-raptor
Raptor is a plasmoid Menu for KDE4

%files -n plasma-applet-raptor
%defattr(-,root,root)
%{_kde_libdir}/kde4/plasma_applet_raptor.so
%{_kde_appsdir}/desktoptheme/default/widgets/overlay.svg
%{_kde_appsdir}/desktoptheme/default/widgets/raptorarrows.svg
%{_kde_datadir}/kde4/services/plasma-applet-raptor.desktop        

#-----------------------------------------------------------------------------

%package -n plasma-engine-raptor
Summary:    Raptor is a plasmoid Menu for KDE4
Group:      Graphical desktop/KDE
Requires:   kdebase4-runtime
Provides:   plasma-engine

%description -n plasma-engine-raptor
Raptor is a plasmoid Menu for KDE4

%files -n plasma-engine-raptor
%defattr(-,root,root)
%{_kde_libdir}/kde4/plasma_engine_raptor.so
%{_kde_datadir}/kde4/services/plasma-engine-raptor.desktop

#-----------------------------------------------------------------------------
%prep
%setup -q -n %oname

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
