require 'spec_helper'

describe package('numpy') do
  it { should be_installed.by('pip3').with_version('1.18.4') }
end

describe package('pandas') do
  it { should be_installed.by('pip3').with_version('1.0.3') }
end

describe package('python-dateutil') do
  it { should be_installed.by('pip3').with_version('2.8.1') }
end

describe package('pytz') do
  it { should be_installed.by('pip3').with_version('2020.1') }
end

describe package('scipy') do
  it { should be_installed.by('pip3').with_version('1.4.1') }
end

describe package('six') do
  it { should be_installed.by('pip3').with_version('1.14.0') }
end