import { gsap } from "gsap";
import { SplitText } from "gsap/SplitText";

gsap.registerPlugin(SplitText);

export default defineNuxtPlugin(() => {
  return {
    provide: {
      gsap,
      SplitText,
    },
  };
});