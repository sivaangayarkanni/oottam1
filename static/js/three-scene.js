let scene, camera, renderer, trees = [], particles = [];
let animationId;

function initForest() {
    const container = document.getElementById('three-container');
    if (!container) return;
    
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0xFAF7F2);
    scene.fog = new THREE.Fog(0xFAF7F2, 5, 50);
    
    camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 5, 20);
    camera.lookAt(0, 2, 0);
    
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);
    
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);
    
    const directionalLight = new THREE.DirectionalLight(0xD4A574, 0.8);
    directionalLight.position.set(10, 20, 10);
    scene.add(directionalLight);
    
    createTrees();
    createGround();
    createParticles();
    
    window.addEventListener('resize', onWindowResize);
    
    animate();
}

function createTrees() {
    const treeColors = [0x1B4332, 0x2D6A4F, 0x40916C];
    
    for (let i = 0; i < 30; i++) {
        const tree = createTree(treeColors[Math.floor(Math.random() * treeColors.length)]);
        
        const x = (Math.random() - 0.5) * 60;
        const z = (Math.random() - 0.5) * 30 - 5;
        const scale = 0.5 + Math.random() * 1.5;
        
        tree.position.set(x, 0, z);
        tree.scale.set(scale, scale * (0.8 + Math.random() * 0.4), scale);
        
        tree.rotation.y = Math.random() * Math.PI * 2;
        
        trees.push({ mesh: tree, speed: 0.0005 + Math.random() * 0.001 });
        scene.add(tree);
    }
}

function createTree(color) {
    const group = new THREE.Group();
    
    const trunkGeometry = new THREE.CylinderGeometry(0.15, 0.25, 2, 8);
    const trunkMaterial = new THREE.MeshLambertMaterial({ color: 0x5C4033 });
    const trunk = new THREE.Mesh(trunkGeometry, trunkMaterial);
    trunk.position.y = 1;
    group.add(trunk);
    
    const foliageColors = [
        new THREE.MeshLambertMaterial({ color: color }),
        new THREE.MeshLambertMaterial({ color: 0x2D6A4F }),
        new THREE.MeshLambertMaterial({ color: 0x40916C })
    ];
    
    for (let i = 0; i < 3; i++) {
        const coneGeometry = new THREE.ConeGeometry(1.5 - i * 0.3, 2 - i * 0.3, 8);
        const cone = new THREE.Mesh(coneGeometry, foliageColors[i % 3]);
        cone.position.y = 2.5 + i * 1.2;
        group.add(cone);
    }
    
    return group;
}

function createGround() {
    const groundGeometry = new THREE.PlaneGeometry(100, 100);
    const groundMaterial = new THREE.MeshLambertMaterial({ 
        color: 0xE8E4DE,
        side: THREE.DoubleSide
    });
    const ground = new THREE.Mesh(groundGeometry, groundMaterial);
    ground.rotation.x = -Math.PI / 2;
    ground.position.y = -0.1;
    scene.add(ground);
}

function createParticles() {
    const particleGeometry = new THREE.BufferGeometry();
    const particleCount = 100;
    
    const positions = new Float32Array(particleCount * 3);
    const colors = new Float32Array(particleCount * 3);
    
    const leafColor = new THREE.Color(0x40916C);
    const goldColor = new THREE.Color(0xD4A574);
    
    for (let i = 0; i < particleCount; i++) {
        positions[i * 3] = (Math.random() - 0.5) * 50;
        positions[i * 3 + 1] = Math.random() * 15;
        positions[i * 3 + 2] = (Math.random() - 0.5) * 30 - 5;
        
        const color = Math.random() > 0.5 ? leafColor : goldColor;
        colors[i * 3] = color.r;
        colors[i * 3 + 1] = color.g;
        colors[i * 3 + 2] = color.b;
    }
    
    particleGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    particleGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
    
    const particleMaterial = new THREE.PointsMaterial({
        size: 0.15,
        vertexColors: true,
        transparent: true,
        opacity: 0.7,
        sizeAttenuation: true
    });
    
    const particleSystem = new THREE.Points(particleGeometry, particleMaterial);
    particles.push({ mesh: particleSystem, speed: 0.002 });
    scene.add(particleSystem);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
    animationId = requestAnimationFrame(animate);
    
    const time = Date.now() * 0.001;
    
    trees.forEach(tree => {
        tree.mesh.rotation.z = Math.sin(time * tree.speed * 100 + tree.mesh.position.x) * 0.02;
    });
    
    particles.forEach(particle => {
        const positions = particle.mesh.geometry.attributes.position.array;
        
        for (let i = 0; i < positions.length; i += 3) {
            positions[i + 1] += Math.sin(time + i) * 0.002;
            positions[i] += Math.cos(time * 0.5 + i) * 0.001;
            
            if (positions[i + 1] > 15) {
                positions[i + 1] = 0;
            }
        }
        
        particle.mesh.geometry.attributes.position.needsUpdate = true;
    });
    
    camera.position.x = Math.sin(time * 0.1) * 2;
    camera.position.y = 5 + Math.sin(time * 0.15) * 0.5;
    camera.lookAt(0, 3, 0);
    
    renderer.render(scene, camera);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initForest);
} else {
    initForest();
}
