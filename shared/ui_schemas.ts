export interface Message {
  id: string;
  text: string;
  sender: 'user' | 'jarvis';
  timestamp: number;
}

export interface JarvisColors {
  primary: string;
  surface: string;
  text: string;
  glow: string;
}

export const motionConfig = {
  timing: {
    base: 300,
    smooth: 600
  },
  easing: [0.4, 0, 0.2, 1]
};

export interface ChatScreenConfig {
  showIndicators: boolean;
  blurEffect: boolean;
  fpsLimit: 60;
}
